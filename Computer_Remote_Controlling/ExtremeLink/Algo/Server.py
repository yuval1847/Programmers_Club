import socket
import threading
import mouse
import keyboard

class Server:
    """A class which represent the server."""

    def __init__(self) -> None:

        # The input socket.
        self.IN_PORT = 1234
        self.inputSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.inputSocket.bind(("0.0.0.0", self.IN_PORT))
        self.inputSocket.listen(1)
        print(f"Server's input socket is listening on port {self.IN_PORT}...")
        self.clientInputSocket, self.clientAddr = self.inputSocket.accept()

        # The frames socket.
        self.F_PORT = 1847
        self.framesSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.framesSocket.bind(("0.0.0.0", self.F_PORT))
        self.framesSocket.listen(1)
        print(f"Server's frames socket is listening on port {self.F_PORT}...")
        self.clientFramesSocket = self.framesSocket.accept()[0]

        print(f"The client {self.clientAddr} succssefully connected!")

        # Threads and Mutex Lock
        self.mutexLock = threading.Lock()
        self.inputThread = threading.Thread(target=)
        self.framesThread = threading.Thread(target=)

        self.inputThread.start()
        self.framesThread.start()


    # The mouse functions:

    def GetMousePos(self):
        # The function gets nothing.
        # The function returns the current position of the mouse on the screen as a tuple of x and y.
        return mouse.get_position()
    

    def SendMousePos(self, pos:tuple[int, int]):
        # The function gets a tuple of 2 integers which represent the position of the mouse.
        # The function sends the position to the client as a binary sequence.
        self.clientInputSocket.send("mouse".encode())
        self.clientInputSocket.send(tuple[0].encode())
        self.clientInputSocket.send(tuple[1].encode())

    
    # The keyboard functions:

    def FilterOneKeyOrCombination(self):
        # The function gets nothing.
        # The functino returns the 


    def GetKeyboardIn(self):
        # The function gets nothing.
        # The function returns the input of keyboard as a string.
        pass
        # Complete this later:
        #return keyboard.on_press()