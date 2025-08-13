from typing import List, Dict, Any
import re

BILL_PATTERNS = [
    r"amount due", r"statement", r"invoice", r"due\s+on", r"pay by", r"total due", r"billing"
]
MEETING_PATTERNS = [
    r"meeting", r"invite", r"calendar", r"zoom", r"google meet", r"teams", r"when:", r"agenda"
]
SUB_PATTERNS = [
    r"unsubscribe", r"manage subscription", r"renewal", r"trial", r"auto-?renew", r"cancel"
]


def extract_tasks(text: str) -> Dict[str, List[str]]:
    """
    Rule-based extractor that scans the input text for predefined patterns
    and returns any matches grouped by task category.
    Categories: 'billing', 'meeting', 'subscription'.
    """
    results: Dict[str, List[str]] = {}
    categories = {
        'billing': BILL_PATTERNS,
        'meeting': MEETING_PATTERNS,
        'subscription': SUB_PATTERNS,
    }
    for category, patterns in categories.items():
        matches: List[str] = []
        for pattern in patterns:
            found = re.findall(pattern, text, flags=re.IGNORECASE)
            if found:
                matches.extend(found)
        if matches:
            results[category] = matches
    return results