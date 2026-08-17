import json

from dataclasses import asdict, is_dataclass
from datetime import date, datetime
from decimal import Decimal
from enum import Enum

from falcon_core.constants.event_constants import (
    EVENT_VERSION as CORE_EVENT_VERSION,
    EVENT_SOURCE_FORGE
)

from falcon_core.utils.event_id import (
    EventIdGenerator
)


class EventBuilder:

    EVENT_VERSION = CORE_EVENT_VERSION
    EVENT_SOURCE = EVENT_SOURCE_FORGE

    @staticmethod
    def build(
        event_type,
        payload,
        correlation_id
    ):

        if is_dataclass(payload):

            payload = asdict(payload)

        event = {
            "eventId": EventIdGenerator.generate(),
            "eventType": event_type,
            "eventVersion": EventBuilder.EVENT_VERSION,
            "eventSource": EventBuilder.EVENT_SOURCE,
            "eventTimestamp": (
                datetime.now()
                .astimezone()
                .isoformat()
            ),
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

        if isinstance(
            value,
            (datetime, date)
        ):

            return value.isoformat()

        if isinstance(value, Decimal):

            return str(value)

        if isinstance(value, Enum):

            return value.value

        raise TypeError(
            f"Object of type "
            f"{type(value).__name__} "
            f"is not JSON serializable"
        )