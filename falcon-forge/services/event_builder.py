from models.domain.event import Event


class EventBuilder:

    @staticmethod
    def build(event_type: str, payload):

        return Event.create(
            event_type=event_type,
            payload=payload
        )