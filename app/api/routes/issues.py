from fastapi import APIRouter


router = APIRouter()
@router.get("/")
def get_issues():
    return {"message": "All issues"}