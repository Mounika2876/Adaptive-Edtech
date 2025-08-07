from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Activity(BaseModel):
    user_id: str
    activity_type: str
    timestamp: str
    metadata: dict

@router.post("/track")
def track_activity(activity: Activity):
    return {"status": "activity logged", "data": activity}

@router.get("/profile/{user_id}")
def get_profile(user_id: str):
    return {"user_id": user_id, "profile": "Sample learner profile"}    
