from fastapi import APIRouter
from services.personalization import recommend_content

router = APIRouter()

@router.get("/recommend/{user_id}")
def get_recommendation(user_id: str):
    return recommend_content(user_id)
    