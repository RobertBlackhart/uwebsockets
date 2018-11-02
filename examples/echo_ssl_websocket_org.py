import uwebsockets.client
uri = "wss://echo.websocket.org/"
websocket = uwebsockets.client.connect(uri)
print("Connecting to {}:".format(uri))
mesg = "The quick brown fox jumps over the lazy dog"
websocket.send(mesg + "\r\n")
resp = websocket.recv()
print(resp)
assert(mesg + "\r\n" == resp)
