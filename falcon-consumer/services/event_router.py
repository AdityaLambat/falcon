class EventRouter:

    ROUTES = {
        "falcon_Customer": "customer",
        "falcon_Account": "account",
        "falcon_Beneficiary": "beneficiary",
        "falcon_CustomerDevice": "customer_device",
        "falcon_Transaction": "transaction"
    }

    @staticmethod
    def route(event_type, payload):

        if event_type not in EventRouter.ROUTES:

            raise ValueError(
                f"Unsupported eventType: {event_type}"
            )

        domain = EventRouter.ROUTES[event_type]

        return domain, payload