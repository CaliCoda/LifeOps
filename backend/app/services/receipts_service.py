from typing import List, Optional, Dict, Any
from sqlmodel import select
from datetime import datetime
from .storage import Receipt, get_session

def create_receipt(items: List[Dict[str, Any]]) -> Receipt:
    """
    Create a new receipt with the given list of item dicts.
    """
    with get_session() as session:
        receipt = Receipt(items=items)
        session.add(receipt)
        session.commit()
        session.refresh(receipt)
        return receipt

def append_to_receipt(receipt_id: int, new_items: List[Dict[str, Any]]) -> Optional[Receipt]:
    """
    Append new items to an existing receipt. Returns the updated receipt, or None if not found.
    """
    with get_session() as session:
        statement = select(Receipt).where(Receipt.id == receipt_id)
        result = session.exec(statement)
        receipt = result.one_or_none()
        if receipt is None:
            return None
        receipt.items.extend(new_items)
        receipt.updated_at = datetime.utcnow()
        session.add(receipt)
        session.commit()
        session.refresh(receipt)
        return receipt

def get_receipt(receipt_id: int) -> Optional[Receipt]:
    """
    Retrieve a receipt by its ID.
    """
    with get_session() as session:
        return session.get(Receipt, receipt_id)

def list_receipts() -> List[Receipt]:
    """
    Retrieve all receipts.
    """
    with get_session() as session:
        return session.exec(select(Receipt)).all()