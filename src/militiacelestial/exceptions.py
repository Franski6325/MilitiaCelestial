"""MilitiaCelestial-specific exceptions."""


class MilitiaCelestialError(Exception):
    """Base error for MilitiaCelestial."""


class MappingError(MilitiaCelestialError):
    """Invalid or unreadable mapping YAML."""


class IdRangeExhaustedError(MilitiaCelestialError):
    """No remaining Wazuh rule IDs in the configured range."""


class ValidationError(MilitiaCelestialError):
    """XML or Wazuh smoke-test validation failed."""


class DownloadError(MilitiaCelestialError):
    """SigmaHQ download failed."""


class UnsupportedConversionError(MilitiaCelestialError):
    """A Sigma construct cannot be expressed in the Wazuh target."""
