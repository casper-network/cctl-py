import enum
import os


class EVarType(enum.Enum):
    """Enumeration over set of supported environment variables.
    
    """
    # Root folder of CCTL installation.
    CCTL = "CCTL"


def get_evar(evar: EVarType) -> object:
    """Returns an environment variable.
    
    :param evar: Type of environment variable.
    :returns: Environment variable value.

    """
    return os.getenv(evar.name)
