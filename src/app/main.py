from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.app.db import init_db
from src.app.endpoints import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    init_db()
    yield


def create_app():
    app = FastAPI(
        title="AI FAQ API",
        lifespan=lifespan
    )
    app.include_router(router)
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
