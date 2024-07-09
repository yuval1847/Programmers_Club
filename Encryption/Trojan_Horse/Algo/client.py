import socket
import SSL_Socket

class Client:
    """A class which represent a client."""
    def __init__(self) -> None:
        self.clientSocket = SSL_Socket.SslSocket(isServer=False, sourceIp="localhost", sourcePort=1234, certFilePath="cert.crt")
        self.secretWord = self.clientSocket.GetMsg()
        print(self.secretWord)


if __name__ == "__main__":
    clientObject = Client()
