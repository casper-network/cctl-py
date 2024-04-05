import enum


class AssymetricKeyType(enum.Enum):
    """Enumeration over set of assymmetric key types.
    
    """
    PRIVATE = enum.auto()
    PUBLIC = enum.auto()


class AccountType(enum.Enum):
    """Enumeration over set of CCTL account types.
    
    """
    FAUCET = enum.auto()
    USER = enum.auto()
    VALIDATOR = enum.auto()


class NodePortType(enum.Enum):
    """Enumeration over set of node port types.
    
    """
    RPC = enum.auto()
    RPC_SPECULATIVE = enum.auto()
    REST = enum.auto()
    SSE = enum.auto()
