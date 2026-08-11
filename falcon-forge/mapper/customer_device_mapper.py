from datetime import datetime

from models.domain.customer_device import CustomerDevice
from models.enums.device_status import DeviceStatus


class CustomerDeviceMapper:

    @staticmethod
    def map_to_customer_device(row):

        registered_at = None

        if row.get("registeredAt"):
            registered_at = datetime.fromisoformat(
                row["registeredAt"]
            )

        return CustomerDevice(
            deviceId=int(row["deviceId"]),
            customerId=int(row["customerId"]),
            deviceIdentifier=row["deviceIdentifier"],
            registeredAt=registered_at,
            lastSeenAt=datetime.fromisoformat(
                row["lastSeenAt"]
            ),
            deviceStatus=DeviceStatus(
                row["deviceStatus"]
            )
        )