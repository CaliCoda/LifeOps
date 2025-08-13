from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, List, Dict, Any
from contextlib import contextmanager
from sqlalchemy import Column, JSON
import os
from datetime import datetime


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./lifeops.db")
engine = create_engine(DATABASE_URL, echo=True)


class Email(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sender: str
    subject: str
    recipients: List[str] = Field(default_factory=list, sa_column=Column(JSON))
    body: str
    date: datetime = Field(default_factory=datetime.utcnow)


class Action(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    params: Dict[str, Any] = Field(default_factory=dict, sa_column=Column(JSON))
    proposed_at: datetime = Field(default_factory=datetime.utcnow)
    executed_at: Optional[datetime] = Field(default=None)
    status: str = Field(default="pending")


class Receipt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    items: List[Dict[str, Any]] = Field(default_factory=list, sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Secret(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    secret_name: str
    secret_value: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


def init_db() -> None:
    """Initialize database, creating all tables."""
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session() -> Session:
    """Provide a transactional scope around a series of operations."""
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()