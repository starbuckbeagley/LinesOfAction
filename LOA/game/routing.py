from channels.routing import route
from .consumers import ws_receive, ws_add, ws_disconnect


channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_receive),
    route("websocket.disconnect", ws_disconnect),
]
