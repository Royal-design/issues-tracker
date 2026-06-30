from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.enums.issues import IssuePriority, IssueStatus


    
class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    status: IssueStatus = Field(default=IssueStatus.open)
    priority: IssuePriority = Field(default=IssuePriority.medium)
    
class IssueUpdate(BaseModel):
    title:Optional[str] = Field(default=None, max_length=100)
    description:Optional[str] = Field(default=None, max_length=1000)
    status:Optional[IssueStatus] = None
    priority:Optional[IssuePriority] = None

class IssueOut(BaseModel):
    id: int
    title: str
    description: str
    status: IssueStatus
    priority: IssuePriority
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)