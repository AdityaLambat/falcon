from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from decimal import Decimal
from enum import Enum
from typing import Any
from uuid import uuid4


@dataclass
class Event:
    eventId: str
    eventType: str
    eventVersion: str
    eventSource: str
    eventTimestamp: datetime
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
        return self._serialize(asdict(self))

    @staticmethod
    def _serialize(value):

        if isinstance(value, Enum):
            return value.value

        if isinstance(value, datetime):
            return value.isoformat()

        if isinstance(value, Decimal):
            return str(value)

        if isinstance(value, dict):
            return {
                key: Event._serialize(item)
                for key, item in value.items()
            }

        if isinstance(value, list):
            return [
                Event._serialize(item)
                for item in value
            ]

        if isinstance(value, tuple):
            return [
                Event._serialize(item)
                for item in value
            ]

        return value