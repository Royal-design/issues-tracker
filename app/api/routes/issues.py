from fastapi import APIRouter, Depends, HTTPException
from httpx import get
from sqlalchemy.orm import Session
from app.database import  get_db

from app.models.issues import Issue
from app.schemas.issues import IssueCreate, IssueUpdate



router = APIRouter()
@router.get("/")
def get_issues(db: Session = Depends(get_db)):
    return db.query(Issue).all()

@router.get("/{id}")
def get_issue(id:int, db: Session = Depends(get_db)):
    issue = db.query(Issue).filter(Issue.id==id).first()
    if issue:
        return issue
    else:
        raise HTTPException(status_code=404, detail="Issue not found")

@router.post("/")
def create_issue(issue:IssueCreate, db: Session = Depends(get_db)):
    db_issue = Issue(**issue.model_dump())
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return  db_issue

@router.put("/{id}")
def update_issue(id:int, issue:IssueUpdate, db: Session = Depends(get_db)):
  db_issue = get_issue(id, db)
  updated_issue = issue.model_dump()
  
  for key, value in updated_issue.items():
      setattr(db_issue, key, value)
  db.commit()
  db.refresh(db_issue)
  return db_issue

@router.delete("/{id}")
def delete_issue(id:int, db: Session = Depends(get_db)):
    db_issue = get_issue(id, db)
    db.delete(db_issue)
    db.commit()
    return {"message": "Issue deleted successfully"}