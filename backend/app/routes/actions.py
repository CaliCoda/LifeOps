from datetime import datetime
from typing import List, Optional, Dict, Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.actions_service import(
    propose_action,
    execute_action,
    get_action,
    list_actions,
)

router = APIRouter(prefix="/api/v1/actions", tags=["actions"])


class ProposeRequest(BaseModel):
    name: str
    params: Dict[str, Any]
    delay_seconds: Optional[int] = None


class ActionResponse(BaseModel):
    id: int
    name: str
    params: Dict[str, Any]
    proposed_at: datetime
    executed_at: Optional[datetime]
    status: str


@router.post("/propose", response_model=ActionResponse)
def propose(request: ProposeRequest) -> ActionResponse:
    return propose_action(request.name, request.params, request.delay_seconds)


@router.post("/{action_id}/execute", response_model=ActionResponse)
def execute(action_id: int) -> ActionResponse:
    action = execute_action(action_id)
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    return action


@router.get("/", response_model=List[ActionResponse])
def get_all() -> List[ActionResponse]:
    return list_actions()


@router.get("/{action_id}", response_model=ActionResponse)
def get_one(action_id: int) -> ActionResponse:
    action = get_action(action_id)
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    return action