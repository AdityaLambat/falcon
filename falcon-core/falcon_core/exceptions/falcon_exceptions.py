class FalconException(Exception):
    """Base exception for Falcon."""

    pass


class FalconConfigurationException(FalconException):
    """Raised when Falcon configuration is invalid."""

    pass


class FalconEventException(FalconException):
    """Raised when an event is invalid."""

    pass


class FalconPersistenceException(FalconException):
    """Raised when persistence fails."""

    pass


class FalconKafkaException(FalconException):
    """Raised when a Kafka operation fails."""

    pass