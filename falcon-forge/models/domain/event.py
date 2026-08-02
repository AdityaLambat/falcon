from dataclasses import dataclass, asdict
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4


@dataclass
class Event:
    eventId: str
    eventType: str
    eventVersion: str
    eventSource: str
    eventTimestamp: str
    correlationId: str
    payload: Any

    @classmethod
    def create(
        cls,
        event_type: str,
        payload: Any,
        event_source: str = "Falcon Forge",
        event_version: str = "1.0",
        correlation_id: str | None = None
    ):
        return cls(
            eventId=str(uuid4()),
            eventType=event_type,
            eventVersion=event_version,
            eventSource=event_source,
            eventTimestamp=datetime.now(UTC).isoformat(),
            correlationId=correlation_id or str(uuid4()),
            payload=payload
        )

    def to_dict(self):
        return asdict(self)