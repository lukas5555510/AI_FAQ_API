from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from src.app.service_open_ai import ServiceOpenAi
from src.app.schema import ChatRequest
router = APIRouter()


@router.post("/ask")
async def ask_post(request: ChatRequest, service_openai: ServiceOpenAi = Depends()):
    return StreamingResponse(service_openai.openai_response(request), media_type="text/plain")
