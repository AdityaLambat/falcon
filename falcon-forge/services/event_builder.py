import json
from dataclasses import asdict, is_dataclass
from datetime import date, datetime, UTC
from decimal import Decimal
from enum import Enum
from uuid import uuid4

from config.kafka_config import (
    EVENT_VERSION,
    EVENT_SOURCE
)


class EventBuilder:

    @staticmethod
    def build(event_type, payload, correlation_id):

        event = {
            "eventId": str(uuid4()),
            "eventType": event_type,
            "eventVersion": EVENT_VERSION,
            "eventSource": EVENT_SOURCE,
            "eventTimestamp": datetime.now(UTC),
            "correlationId": correlation_id,
            "payload": payload
        }

        return EventBuilder._serialize(event)

    @staticmethod
    def _serialize(data):

        return json.loads(
            json.dumps(
                data,
                default=EventBuilder._json_serializer
            )
        )

    @staticmethod
    def _json_serializer(value):

        if is_dataclass(value):
            return asdict(value)

        if isinstance(value, (datetime, date)):
            return value.isoformat()

        if isinstance(value, Decimal):
            return str(value)

        if isinstance(value, Enum):
            return value.value

        raise TypeError(
            f"Object of type {type(value).__name__} "
            f"is not JSON serializable"
        )