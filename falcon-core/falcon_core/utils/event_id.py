from uuid import uuid4


class EventIdGenerator:

    @staticmethod
    def generate() -> str:

        return str(uuid4())