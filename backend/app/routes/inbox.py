from datetime import datetime
from typing import List, Dict, Any

from fastapi import APIRouter
from sqlmodel import select

from app.services.storage import get_session, Email

router = APIRouter(prefix="/api/v1/inbox", tags=["inbox"])


@router.get("/", response_model=List[Dict[str, Any]])
def list_inbox() -> List[Dict[str, Any]]:
    """
    Retrieve all emails in the inbox.
    """
    with get_session() as session:
        emails = session.exec(select(Email)).all()
        return [email.dict() for email in emails]