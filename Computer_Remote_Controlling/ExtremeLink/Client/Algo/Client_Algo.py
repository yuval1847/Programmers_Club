import socket
import threading
from PIL import Image, ImageTk, ImageGrab
import gzip
import io

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
        # self.mutexLock = threading.Lock()
        # self.inputThread = threading.Thread(target=)
        # self.framesThread = threading.Thread(target=)


    # Server input handling.

    def ReadServerInput():
        # The function gets nothing.
        # The fucntion returns the given input from the server as a string.
        pass

    
    def ApplyInput(inp:str):
        # The function gets the input as a string input.
        # The function apply the input on the client side.
        pass


    # Frames handling.

    def TakeScreenShot(self, topLeft:tuple[int, int], buttomRight:tuple[int, int]):
        # The function gets 2 points, as tuple of integers, which indicates the image sides.
        # The fucntion take a screen shot and return it as an Image Object.
        return ImageGrab.grab(bbox=topLeft+buttomRight)

    
    def CompressImage(self, img:Image):
        # The fucntion gets an image object.
        # The fucntion returns a byte object which represent the given object after getting compressed.
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()
        return gzip.compress(imgByteArr)
    

    def SendFrame(self, compressedFrame:bytes):
        # The function gets a compressed image object.
        # The function sends the compressed object and it's size to the server.
        compressedFrameBytesSize = len(compressedFrame)
        self.framesScoket.send(str(compressedFrameBytesSize).encode())
        self.framesScoket.sendall(compressedFrame)