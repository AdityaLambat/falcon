from datetime import datetime

from falcon_core.logging.logging_service import (
    LoggingService
)

from services.event_router import EventRouter


class EventProcessor:

    REQUIRED_FIELDS = {
        "eventId",
        "eventType",
        "eventVersion",
        "eventSource",
        "eventTimestamp",
        "correlationId",
        "payload"
    }

    def __init__(self):

        self.logger = LoggingService()

    def process(self, event):

        self._validate_event_structure(event)

        correlation_id = event["correlationId"]
        event_type = event["eventType"]

        self._validate_event_timestamp(
            event["eventTimestamp"],
            correlation_id
        )

        domain, payload = EventRouter.route(
            event_type,
            event["payload"]
        )

        return {
            "eventId": event["eventId"],
            "eventType": event_type,
            "eventVersion": event["eventVersion"],
            "eventSource": event["eventSource"],
            "eventTimestamp": event["eventTimestamp"],
            "correlationId": correlation_id,
            "domain": domain,
            "payload": payload
        }

    def _validate_event_structure(self, event):

        if not isinstance(event, dict):

            raise ValueError(
                "Event must be a JSON object."
            )

        missing_fields = (
            self.REQUIRED_FIELDS - event.keys()
        )

        if missing_fields:

            raise ValueError(
                f"Missing event fields: "
                f"{', '.join(sorted(missing_fields))}"
            )

        for field in [
            "eventId",
            "eventType",
            "eventVersion",
            "eventSource",
            "correlationId"
        ]:

            if not event[field]:

                raise ValueError(
                    f"{field} is mandatory."
                )

        if event["eventType"] not in EventRouter.ROUTES:

            raise ValueError(
                f"Unsupported eventType: "
                f"{event['eventType']}"
            )

        if event["payload"] is None:

            raise ValueError(
                f"Payload is missing for eventType: "
                f"{event['eventType']}"
            )

    def _validate_event_timestamp(
        self,
        timestamp,
        correlation_id
    ):

        try:

            datetime.fromisoformat(
                timestamp.replace(
                    "Z",
                    "+00:00"
                )
            )

        except (
            ValueError,
            AttributeError
        ):

            self.logger.error(
                "Invalid eventTimestamp.",
                "UNKNOWN",
                correlation_id
            )

            raise ValueError(
                "Invalid eventTimestamp."
            )