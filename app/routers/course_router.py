from fastapi import APIRouter
from app.controllers.course_controller import get_all_courses

router = APIRouter()

@router.get("/")
def fetch_courses():
    return get_all_courses()
