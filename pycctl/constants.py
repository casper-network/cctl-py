import typing

from pycctl.types import AssymetricKeyType


# Map: Assymmetric file tyoe <-> file name.
ASSYMETRIC_KEY_FNAME: typing.Dict[AssymetricKeyType, str] = {
    AssymetricKeyType.PRIVATE: "secret_key.pem",
    AssymetricKeyType.PUBLIC: "public_key_hex",
}

# Default base ports.
BASE_PORT_REST: int = 14100
BASE_PORT_RPC: int = 11100
BASE_PORT_SPEC_EXEC: int = 25100
BASE_PORT_SSE: int = 18100

# Default chain name.
CHAIN_NAME: str = "cspr-dev-cctl"

# Default number of nodes.
COUNT_OF_NODES: int = 10

# Default number of test users.
COUNT_OF_USERS: int = 10

# Default protocol version ... genesis.
PROTOCOL_VERSION: str = "1_0_0"

# Set of network level binaries.
NET_BINARIES: typing.Set[str] = {
    "activate_bid.wasm",
    "add_bid.wasm",
    "casper-client",
    "delegate.wasm",
    "transfer_to_account_u512.wasm",
    "undelegate.wasm",
    "withdraw_bid.wasm",
}

# Set of network level config files.
NET_CONFIG: typing.Set[str] = {
    "genesis/accounts.toml",
    "genesis/chainspec.toml",
}

# Set of node level binaries.
NODE_BINARIES: typing.Set[str] = {
    f"{PROTOCOL_VERSION}/casper-node",
    "casper-node-launcher",
}

# Set of node config files.
NODE_CONFIG: typing.Set[str] = {
    f"{PROTOCOL_VERSION}/accounts.toml",
    f"{PROTOCOL_VERSION}/chainspec.toml",
    f"{PROTOCOL_VERSION}/config.toml",
}

# Default node ordinal identfier.
NODE_IDX: int = 1

# Default payment amount for smart contract installation.
SC_PAYMENT_INSTALL: int = int(50e9)
