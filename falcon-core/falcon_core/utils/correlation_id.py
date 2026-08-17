from uuid import uuid4


class CorrelationIdGenerator:

    @staticmethod
    def generate() -> str:

        return str(uuid4())