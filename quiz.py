from fastapi import APIRouter
from pydantic import BaseModel
from services.quiz_engine import generate_quiz

router = APIRouter()

class QuizRequest(BaseModel):
    user_id: str
    topic: str

@router.post("/generate")
def get_quiz(request: QuizRequest):
    return generate_quiz(request.user_id, request.topic)