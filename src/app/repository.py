from src.app.model import PromptData
from sqlalchemy.orm import Session
from fastapi import Depends
from src.app.session import get_db


class PromptRepository:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def save_prompt_data(self, prompt: str, answer: str, model: str, error: str, success: bool) -> PromptData:

        obj = PromptData(
            answer=answer,
            model=model,
            error=error,
            prompt=prompt,
            success=success
        )

        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj
