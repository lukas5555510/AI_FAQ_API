from pydantic import BaseModel
from typing import List


class ChatMessage(BaseModel):
    role: str = "user" # "user", "system", "assistant"
    content: str = "Write in two sentences graphql advantages"


class ChatRequest(BaseModel):
    model: str = "gpt-3.5-turbo"
    messages: List[ChatMessage]
    stream: bool = True  # Toggle for streaming
    max_tokens: int = 512