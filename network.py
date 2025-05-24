import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.IF_INET, socket.SOCK_STREAM)
        self.server = "10.48.8.100"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()
    
    def connect(self):
        self.client.connect(self.addr)
        