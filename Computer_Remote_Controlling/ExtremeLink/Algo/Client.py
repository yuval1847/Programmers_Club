import socket
import threading

class Client:
    """A class which represent the client."""
    def __init__(self, serverAddr) -> None:

        self.serverAddr = serverAddr
        
        # The input socket
        self.IN_PORT = 1234
        self.inputSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.inputSocket.connect((self.serverAddr, self.IN_PORT))

        # The frames socket
        self.F_PORT = 1847
        self.framesScoket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.framesScoket.connect((self.serverAddr, self.F_PORT))

        print(f"Successfully connected to the server!")

        # Threads
        self.mutexLock = threading.Lock()
        self.inputThread = threading.Thread(target=)
        self.framesThread = threading.Thread(target=)


    def ReadServerInput():
        # The function gets nothing.
        # The fucntion returns the given input from the server as a string.
        pass

    
    def ApplyInput(inp:str):
        # The function gets the input as a string input.
        # The function apply the input on the client side.
        pass
