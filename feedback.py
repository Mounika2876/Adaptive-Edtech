from fastapi import APIRouter
from pydantic import BaseModel
from  services.nlp_analysis import analyze_feedback

router = APIRouter()

class Feedback(BaseModel):
    user_id: str
    text: str

@router.post("/analyze")
def feedback_analysis(feedback: Feedback):
    return analyze_feedback(feedback.text)   