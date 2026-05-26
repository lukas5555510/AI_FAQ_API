from openai import AsyncOpenAI
from dotenv import load_dotenv
from src.app.schema import ChatRequest
from src.app.repository import PromptRepository
from fastapi import Depends
from src.app.session import get_db
from sqlalchemy.orm import Session

load_dotenv()
client = AsyncOpenAI()


class ServiceOpenAi:

    def __init__(self, db: Session = Depends(get_db)):
        self.repo = PromptRepository(db)

    async def openai_response(self, request: ChatRequest):
        formatted_messages = [{"role": m.role, "content": m.content} for m in request.messages]

        prompt_messages = [f"{m.role}:{m.content}\n><\n" for m in request.messages]
        chunks = []
        error_message = None

        try:
            stream = await client.chat.completions.create(
                model=request.model,
                messages=formatted_messages,
                max_tokens=request.max_tokens,
                stream=True
            )

            async for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    chunks.append(delta)
                    yield delta

        except Exception as e:
            error_message = str(e)
            print(f"Streaming error: {e}")
            yield f"\n[Error: {str(e)}]"
        finally:
            full_response = "".join(chunks)
            full_prompt = "".join(prompt_messages)
            success = True
            if error_message:
                full_response+=f"\n\n [STREAM_ERROR]: {error_message}"
                success = False

            try:
                self.repo.save_prompt_data(answer=full_response, prompt=full_prompt, model=request.model, error=error_message, success=success)

            except Exception as db_error:
                print(f"Database save error: {db_error}")

