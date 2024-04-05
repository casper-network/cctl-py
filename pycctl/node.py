from pycspr.api.rest import Client as RestClient
from pycspr.api.rest import ConnectionInfo as RestConnectionInfo
from pycspr.api.rpc import Client as RpcClient
from pycspr.api.rpc import ConnectionInfo as RpcConnectionInfo
from pycspr.api.rpc_speculative import Client as RpcSpeculativeClient
from pycspr.api.rpc_speculative import ConnectionInfo as RpcSpeculativeConnectionInfo
from pycspr.api.sse import Client as SseClient
from pycspr.api.sse import ConnectionInfo as SseConnectionInfo
from pycctl.constants import BASE_PORT_REST
from pycctl.constants import BASE_PORT_RPC
from pycctl.constants import BASE_PORT_SPEC_EXEC
from pycctl.constants import BASE_PORT_SSE
from pycctl.types import NodePortType


_PORT_BY_TYPE = {
    NodePortType.REST: BASE_PORT_REST,
    NodePortType.RPC: BASE_PORT_RPC,
    NodePortType.RPC_SPECULATIVE: BASE_PORT_SPEC_EXEC,
    NodePortType.SSE: BASE_PORT_SSE,
}


def get_port(port_type: NodePortType, node_idx: int) -> int:
    """Returns a node's port.
    
    :param port_type: Type of node port.
    :param node_idx: Index of node.
    :returns: A node port.
    
    """
    return _PORT_BY_TYPE[port_type] + node_idx


def get_rest_client(node_idx: int = 1) -> RestClient:
    """Returns a node REST API client.
    
    :param node_idx: Index of node.
    :returns: A node REST API client.
    
    """
    return RestClient(
        RestConnectionInfo(
            port=get_port(NodePortType.REST, node_idx)
        )
    )


def get_rpc_client(node_idx: int = 1) -> RpcClient:
    """Returns a node JSON-RPC API client.
    
    :param node_idx: Index of node.
    :returns: A node JSON-RPC API client.
    
    """
    return RpcClient(
        RpcConnectionInfo(
            port=get_port(NodePortType.RPC, node_idx)
        )
    )


def get_rpc_speculative_client(node_idx: int = 1) -> RpcSpeculativeClient:
    """Returns a node speculative JSON-RPC API client.
    
    :param node_idx: Index of node.
    :returns: A node speculative JSON-RPC API client.
    
    """
    return RpcSpeculativeClient(
        RpcSpeculativeConnectionInfo(
            port=get_port(NodePortType.RPC_SPECULATIVE, node_idx)
        )
    )


def get_sse_client(node_idx: int = 1) -> SseClient:
    """Returns a node SSE API client.
    
    :param node_idx: Index of node.
    :returns: A node SSE API client.
    
    """
    return SseClient(
        SseConnectionInfo(
            port=get_port(NodePortType.SSE, node_idx),
            port_rpc=get_port(NodePortType.RPC, node_idx),
        )
    )
