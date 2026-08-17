from falcon_core.constants.event_constants import (
    EVENT_TYPE_CUSTOMER,
    EVENT_TYPE_ACCOUNT,
    EVENT_TYPE_BENEFICIARY,
    EVENT_TYPE_CUSTOMER_DEVICE,
    EVENT_TYPE_TRANSACTION,
)


class EventRouter:

    ROUTES = {
        EVENT_TYPE_CUSTOMER: "customer",
        EVENT_TYPE_ACCOUNT: "account",
        EVENT_TYPE_BENEFICIARY: "beneficiary",
        EVENT_TYPE_CUSTOMER_DEVICE: "customer_device",
        EVENT_TYPE_TRANSACTION: "transaction"
    }

    @staticmethod
    def route(event_type, payload):

        if event_type not in EventRouter.ROUTES:

            raise ValueError(
                f"Unsupported eventType: {event_type}"
            )

        domain = EventRouter.ROUTES[event_type]

        return domain, payload