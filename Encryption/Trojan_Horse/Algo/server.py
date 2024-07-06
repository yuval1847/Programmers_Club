import socket
import ssl

class Server:
    # A class which represent the server of the program.

    def __init__(self) -> None:
        self.serverSocket = self.CreatingServerSocket()
        self.SslWrapingSocket()
        self.clientSocket, self.clientAddress = self.sslServerSocket.accept()
        self.SendMsg("Connected!")

    
    def CreatingServerSocket(self):
        # The function gets nothing.
        # The function returns a server socket.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("0.0.0.0", 1234))
        s.listen(1)
        return s


    def SslWrapingSocket(self):
        # The function gets nothing.
        # The function wraps the server socket with ssl protocol.

        # Define SSL context
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile='server.crt', keyfile='server.key')

        # Wrap the socket with SSL
        self.sslServerSocket = context.wrap_socket(self.serverSocket, server_side=True)
        print("Server is listening on port 1234...")
    

    def SendMsg(self, content):
        # The function gets the string value.
        # The function sends the given message and the lenth of it to the client.
        self.clientSocket.send(len(str(((len(content)//4)*4)+4)).encode('utf8'))
        self.clientSocket.send(content.encode())


    def Dissconect(self):
        # The function gets nothing.
        # The function closes the socket of the connection with the client.
        self.clientSocket.close()
        self.sslServerSocket.close()
