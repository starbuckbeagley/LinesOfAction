from channels import Group


# Connected to websocket.connect
def ws_add(message):
    # Accept incoming connection
    message.reply_channel.send({"accept": True})
    Group("players").add(message.reply_channel)


# Connected to websocket.receive
def ws_receive(message):
    text = message.content.get('text')
    if text:
        message.reply_channel.send({"text": "You said: {}".format(text)})


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("players").discard(message.reply_channel)
