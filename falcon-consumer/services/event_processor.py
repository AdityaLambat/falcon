from services.logging_service import LoggingService


class EventProcessor:

    SUPPORTED_EVENTS = {
        "falcon_Customer": "CUSTOMER",
        "falcon_Account": "ACCOUNT",
        "falcon_Beneficiary": "BENEFICIARY",
        "falcon_CustomerDevice": "CUSTOMER_DEVICE",
        "falcon_Transaction": "TRANSACTION"
    }

    def __init__(self):

        self.logger = LoggingService()

    def process(self, event):

        correlation_id = event.get(
            "correlationId",
            "UNKNOWN"
        )

        event_type = event.get("eventType")

        if not event_type:

            self.logger.error(
                "eventType is missing.",
                "UNKNOWN",
                correlation_id
            )

            raise ValueError(
                "eventType is missing from event."
            )

        if event_type not in self.SUPPORTED_EVENTS:

            self.logger.error(
                f"Unsupported eventType: {event_type}",
                "UNKNOWN",
                correlation_id
            )

            raise ValueError(
                f"Unsupported eventType: {event_type}"
            )

        domain = self.SUPPORTED_EVENTS[event_type]

        payload = event.get("payload")

        if payload is None:

            self.logger.error(
                "Payload is missing.",
                domain,
                correlation_id
            )

            raise ValueError(
                f"Payload is missing for eventType: {event_type}"
            )

        return domain, correlation_id, payload