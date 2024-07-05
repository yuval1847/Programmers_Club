import socket

class Server:
    # A class which represent the server of the program.

    def __init__(self) -> None:
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind(("0.0.0.0", 1234))
        self.serverSocket.listen(1)

        