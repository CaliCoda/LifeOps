from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, Generator, List, Dict, Any
import os
from datetime import datetime

from sqlalchemy import Column, JSON

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./lifeops.db")

engine = create_engine(DATABASE_URL, echo=True)


class Example(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Receipt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    items: List[Dict[str, Any]] = Field(default_factory=list, sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


def init_db() -> None:
    """
    Initialize the database, creating all tables.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Provide a transactional scope around a series of operations.
    """
    with Session(engine) as session:
        yield session