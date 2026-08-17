from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Event:

    eventId: str
    eventType: str
    eventVersion: str
    eventSource: str
    eventTimestamp: datetime
    correlationId: str
    payload: Any