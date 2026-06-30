from app.database import SessionLocal
from app.enums.issues import IssuePriority, IssueStatus
from app.models.issues import Issue


issues = [
    {
        "title": "Login page bug",
        "description": "Users cannot log in with Google.",
        "status": IssueStatus.open,
        "priority": IssuePriority.high,
        "created_at": "2026-06-30T10:00:00Z",
        "updated_at": "2026-06-30T10:00:00Z",
    },
    {
        "title": "Update dashboard UI",
        "description": "Improve spacing and responsiveness.",
        "status": IssueStatus.in_progress,
        "priority": IssuePriority.medium,
        "created_at": "2026-06-29T09:30:00Z",
        "updated_at": "2026-06-30T08:15:00Z",
    },
    {
        "title": "Fix email notification",
        "description": "Email isn't sent after issue creation.",
        "status": IssueStatus.closed,
        "priority": IssuePriority.low,
        "created_at": "2026-06-28T14:20:00Z",
        "updated_at": "2026-06-29T11:45:00Z",
    },
]

def init_db():
    db = SessionLocal()
    count = db.query(Issue).count()
    if count == 0:
        for issue in issues:
            db.add(Issue(**issue))
        db.commit()
    db.close()

