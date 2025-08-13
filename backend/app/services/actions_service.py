from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

from app.services.storage import Action, get_session
from sqlmodel import select


def propose_action(
    name: str,
    params: Dict[str, Any],
    delay_seconds: Optional[int] = None,
) -> Action:
    """
    Create a new action proposal. Optionally schedule execution after delay_seconds.
    """
    scheduled_time = datetime.utcnow() + timedelta(seconds=delay_seconds) if delay_seconds else datetime.utcnow()
    with get_session() as session:
        action = Action(name=name, params=params, proposed_at=scheduled_time)
        session.add(action)
        session.commit()
        session.refresh(action)
        return action


def execute_action(action_id: int) -> Optional[Action]:
    """
    Mark the specified action as executed now. Returns the updated Action or None if not found.
    """
    with get_session() as session:
        action = session.get(Action, action_id)
        if not action:
            return None
        action.executed_at = datetime.utcnow()
        action.status = "executed"
        session.add(action)
        session.commit()
        session.refresh(action)
        return action


def get_action(action_id: int) -> Optional[Action]:
    """
    Retrieve an action by its ID.
    """
    with get_session() as session:
        return session.get(Action, action_id)


def list_actions() -> List[Action]:
    """
    List all actions in the system.
    """
    with get_session() as session:
        statement = select(Action)
        return session.exec(statement).all()