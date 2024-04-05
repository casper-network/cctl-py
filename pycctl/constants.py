from pycctl.types import AssymetricKeyType


# Map: Assymmetric file tyoe <-> file name.
ASSYMETRIC_KEY_FNAME = {
    AssymetricKeyType.PRIVATE: "secret_key.pem",
    AssymetricKeyType.PUBLIC: "public_key_hex",
}

# Default base ports.
BASE_PORT_REST = 14100
BASE_PORT_RPC = 11100
BASE_PORT_SPEC_EXEC=25100
BASE_PORT_SSE = 18100

# Default chain name.
CHAIN_NAME = "cspr-dev-cctl"

# Default number of nodes.
COUNT_OF_NODES = 10

# Default number of test users.
COUNT_OF_USERS = 10

# Set of network level binaries.
NET_BINARIES = {
    "activate_bid.wasm",
    "add_bid.wasm",
    "casper-client",
    "delegate.wasm",
    "transfer_to_account_u512.wasm",
    "undelegate.wasm",
    "withdraw_bid.wasm",
}

# Set of network level config files.
NET_CONFIG = {
    "genesis/accounts.toml",
    "genesis/chainspec.toml",
}

# Set of node level binaries.
NODE_BINARIES = {
    "1_0_0/casper-node",
    "casper-node-launcher",
}

# Set of node config files.
NODE_CONFIG = {
    "1_0_0/accounts.toml",
    "1_0_0/chainspec.toml",
    "1_0_0/config.toml",
}

# Default payment amount for smart contract installation.
SC_PAYMENT_INSTALL = int(50e9)

