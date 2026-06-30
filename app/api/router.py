from fastapi import APIRouter
from app.api.routes.issues import router as issues_router


router = APIRouter()

router.include_router(issues_router, prefix="/api/v1/issues", tags=["issues"])