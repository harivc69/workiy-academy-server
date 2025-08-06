from fastapi import APIRouter

from app.routers.course_router import router as course_router

router = APIRouter()

# Register all routers here
router.include_router(course_router, prefix="/courses")
