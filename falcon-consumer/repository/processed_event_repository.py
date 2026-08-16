from datetime import UTC, datetime

from psycopg2.extras import Json


class ProcessedEventRepository:

    INSERT_QUERY = """
        INSERT INTO processed_event (
            event_id,
            event_type,
            event_version,
            event_source,
            event_timestamp,
            correlation_id,
            payload,
            processed_at
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s, %s
        )
        ON CONFLICT (event_id)
        DO NOTHING
        RETURNING event_id
    """

    def __init__(self, connection):

        self.connection = connection

    def save(self, event):

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                self.INSERT_QUERY,
                (
                    event["eventId"],
                    event["eventType"],
                    event["eventVersion"],
                    event["eventSource"],
                    event["eventTimestamp"],
                    event["correlationId"],
                    Json(event["payload"]),
                    datetime.now(UTC)
                )
            )

            result = cursor.fetchone()

            return result is not None

        finally:

            cursor.close()