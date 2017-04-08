from mitmproxy import ctx


def configure(options, updated):
    ctx.log.info("general event configure() call")


def done():
    ctx.log.info("general event done() call")


# Using ctx.log here causes python to throw a stack overflow error.
#def log(entry):
#    ctx.log.info("log() call")


def start():
    ctx.log.info("general event start() call")


# This function is called at a regular interval, as expected.
#def tick():
#    ctx.log.info("tick () call")


def clientconnect(root_layer):
    ctx.log.info("connection event clientconnect() call")


def clientdisconnect(root_layer):
    ctx.log.info("connection event clientdisconnect() call")


def next_layer(layer):
    ctx.log.info("connection event next_layer() call")


def serverconnect(server_conn):
    ctx.log.info("connection event serverconnect() call")


def serverdisconnect(server_conn):
    ctx.log.info("connection event serverdisconnect() call")


def http_connect(flow):
    ctx.log.info("HTTP event http_connect() call")


def request(flow):
    ctx.log.info("HTTP event request() call")


def requestheaders(flow):
    ctx.log.info("HTTP event requestheaders() call")


def responseheaders(flow):
    ctx.log.info("HTTP event responseheaders() call")


def response(flow):
    ctx.log.info("HTTP event response() call")


def error(flow):
    ctx.log.info("HTTP event error() call")


def websocket_handshake(flow):
    ctx.log.info("WebSocket event websocket_handshake() call")


def websocket_start(flow):
    ctx.log.info("WebSocket event websocket_start() call")


def websocket_message(flow):
    ctx.log.info("WebSocket event websocket_message() call")


def websocket_end(flow):
    ctx.log.info("WebSocket event websocket_end() call")


def websocket_error(flow):
    ctx.log.info("WebSocket event websocket_error() call")


def tcp_start(flow):
    ctx.log.info("TCP event tcp_start() call")


def tcp_message(flow):
    ctx.log.info("TCP event tcp_message() call")


def tcp_end(flow):
    ctx.log.info("TCP event tcp_end() call")


def tcp_error(flow):
    ctx.log.info("TCP event tcp_error() call")
