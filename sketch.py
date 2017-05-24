"""mitmproxy API.

All kudos go to mitmproxy team!
"""
from mitmproxy import ctx


def configure(options, updated):
    """Called once on startup, and whenever options change.
    """
    ctx.log.info("general event configure() call")
    ctx.log.info(options)
    ctx.log.info(updated)


def done():
    """Called once when the script shuts down, either because it's been
    unloaded, or because the proxy itself is shutting down.
    """
    ctx.log.info("general event done() call")


# Using ctx.log here causes python to throw a stack overflow error.
#def log(entry):
#   """Called whenever an event log is added.
#   """
#   ctx.log.info("log() call")
#   ctx.log.info(entry)


def start():
    """Called once on startup, before any other events. If you return a
    value  from this event, it will replace the current addon. This
    allows you to, "boot into" an addon implemented as a class instance
    from the module level.
    """
    ctx.log.info("general event start() call")


# This function is called at a regular interval, as expected.
#def tick():
#    """Called at a regular sub-second interval as long as the addon is
#    executing.
#    """
#    ctx.log.info("tick () call")


def clientconnect(root_layer):
    """Called when a client initiates a connection to the proxy. Note that a
    connection can correspond to multiple HTTP requests.
    """
    ctx.log.info("connection event clientconnect() call")
    ctx.log.info(root_layer)


def clientdisconnect(root_layer):
    """Called when a client disconnects from the proxy.
    """
    ctx.log.info("connection event clientdisconnect() call")
    ctx.log.info(root_layer)


def next_layer(layer):
    """Called whenever layers are switched. You may change which layer will
    be used by returning a new layer object from this event.
    """
    ctx.log.info("connection event next_layer() call")
    ctx.log.info(layer)


def serverconnect(server_conn):
    """Called before the proxy initiates a connection to the target server.
    Note that a connection can correspond to multiple HTTP requests.
    """
    ctx.log.info("connection event serverconnect() call")
    ctx.log.info(server_conn)


def serverdisconnect(server_conn):
    """Called when the proxy has closed the server connection.
    """
    ctx.log.info("connection event serverdisconnect() call")
    ctx.log.info(server_conn)


def http_connect(flow):
    """Called when we receive an HTTP CONNECT request. Setting a non 2xx
    response on the flow will return the response to the client abort the
    connection. CONNECT requests and responses do not generate the usual
    HTTP handler events. CONNECT requests are only valid in regular and
    upstream proxy modes.
    """
    ctx.log.info("HTTP event http_connect() call")
    ctx.log.info(flow)


def request(flow):
    """Called when a client request has been received.
    """
    ctx.log.info("HTTP event request() call")
    ctx.log.info(flow)


def requestheaders(flow):
    """Called when the headers of a client request have been received, but
    before the request body is read.
    """
    ctx.log.info("HTTP event requestheaders() call")
    ctx.log.info(flow)


def responseheaders(flow):
    """Called when the headers of a server response have been received, but
    before the response body is read.
    """
    ctx.log.info("HTTP event responseheaders() call")
    ctx.log.info(flow)


def response(flow):
    """Called when a server response has been received.
    """
    ctx.log.info("HTTP event response() call")
    ctx.log.info(flow)


def error(flow):
    """Called when a flow error has occurred, e.g. invalid server responses,
    or interrupted connections. This is distinct from a valid server HTTP
    error response, which is simply a response with an HTTP error code.
    """
    ctx.log.info("HTTP event error() call")
    ctx.log.info(flow)


def websocket_handshake(flow):
    """Called when a client wants to establish a WebSocket connection. The
    WebSocket-specific headers can be manipulated to alter the
    handshake. The ``flow`` object is guaranteed to have a non-None
    ``request`` attribute.
    """
    ctx.log.info("WebSocket event websocket_handshake() call")
    ctx.log.info(flow)


def websocket_start(flow):
    """Called when WebSocket connection is established after a successful
    handshake.
    """
    ctx.log.info("WebSocket event websocket_start() call")
    ctx.log.info(flow)


def websocket_message(flow):
    """Called when a WebSocket message is received from the client or server. The
    sender and receiver are identifiable. The most recent message will be
    ``flow.messages[-1]``. The message is user-modifiable. Currently there are
    two types of messages, corresponding to the BINARY and TEXT frame types.
    """
    ctx.log.info("WebSocket event websocket_message() call")
    ctx.log.info(flow)


def websocket_end(flow):
    """Called when WebSocket connection ends.
    """
    ctx.log.info("WebSocket event websocket_end() call")
    ctx.log.info(flow)


def websocket_error(flow):
    """Called when a WebSocket error occurs - e.g. the connection closing
    unexpectedly.
    """
    ctx.log.info("WebSocket event websocket_error() call")
    ctx.log.info(flow)


def tcp_start(flow):
    """Called when TCP streaming starts.
    """
    ctx.log.info("TCP event tcp_start() call")
    ctx.log.info(flow)


def tcp_message(flow):
    """Called when a TCP payload is received from the client or server. The
    sender and receiver are identifiable. The most recent message will be
    ``flow.messages[-1]``. The message is user-modifiable.
    """
    ctx.log.info("TCP event tcp_message() call")
    ctx.log.info(flow)


def tcp_end(flow):
    """Called when TCP streaming ends.
    """
    ctx.log.info("TCP event tcp_end() call")
    ctx.log.info(flow)


def tcp_error(flow):
    """Called when a TCP error occurs - e.g. the connection closing
    unexpectedly.
    """
    ctx.log.info("TCP event tcp_error() call")
    ctx.log.info(flow)
