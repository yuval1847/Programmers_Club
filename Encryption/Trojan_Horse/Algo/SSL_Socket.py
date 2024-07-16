import socket
import ssl

class SslSocket(socket.socket):
    # A class which represents an SSL socket

    def __init__(self, isServer, sourceIp, sourcePort, certFilePath, keyFilePath=None) -> None:
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.isServer = isServer

        if self.isServer:
            self.bind((sourceIp, sourcePort))
            self.listen(1)
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            self.context.load_cert_chain(certfile=certFilePath, keyfile=keyFilePath)
            print("Waiting for a connection...")
            self.sock, self.addr = self.accept()
            print(f"Connection from {self.addr}")
            # Wrap the socket with SSL
            self.sslConnectedSocket = self.context.wrap_socket(self.sock, server_side=True)
        else:
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            self.context.load_verify_locations(cafile=certFilePath)
            self.connect((sourceIp, sourcePort))
            # Wrap the socket with SSL
            self.sslConnectedSocket = self.context.wrap_socket(self, server_hostname=sourceIp)

    def SendMsg(self, content):
        # The function gets the string value.
        # The function sends the length of the message first and then the given message itself.
        try:
            length_bytes = len(content).to_bytes(4, byteorder='big')
            if self.isServer:
                self.sslConnectedSocket.send(length_bytes)
                self.sslConnectedSocket.send(content.encode('utf-8'))
            else:
                self.sslConnectedSocket.send(length_bytes)
                self.sslConnectedSocket.send(content.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")

    def GetMsg(self):
        # The function gets nothing.
        # The function returns the data that was sent.
        try:
            length_bytes = self.sslConnectedSocket.recv(4)
            msgLength = int.from_bytes(length_bytes, byteorder='big')
            msgContent = self.sslConnectedSocket.recv(msgLength).decode()
            return msgContent
        except Exception as e:
            print(f"Error receiving message: {e}")
            return None

    def Disconnect(self):
        # The function gets nothing.
        # The function closes the socket of the connection with the client.
        self.sslConnectedSocket.close()
        self.close()