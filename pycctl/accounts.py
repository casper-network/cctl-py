import typing

from pycctl.fsys import read_account_public_key
from pycctl.node import get_rpc_client
from pycctl.types import AccountType
from pycspr import get_account_hash
from pycspr.types.node import PurseID
from pycspr.types.node import PurseIDType


async def get_account_balance(
    account_type: AccountType,
    account_idx: typing.Optional[int] = None
) -> int:
    """Retrieves an account balance.

    :param account_type: Type of account under which to execute a purse balance query.
    :param account_idx: For node/user accounts, the account ordinal identifier.
    :returns: An account balance denominated in motes.

    """
    account_key: bytes = read_account_public_key(account_type, account_idx)

    return await get_rpc_client().get_account_balance(
        PurseID(get_account_hash(account_key), PurseIDType.ACCOUNT_HASH)
        )
