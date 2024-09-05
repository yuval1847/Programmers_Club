import socket
import mouse
import keyboard
from PIL import Image, ImageTk
import gzip
import io
import customtkinter

class Server:
    """A class which represent the server."""

    def __init__(self) -> None:
        # The input socket.
        self.IN_PORT = 1234
        self.inputSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.inputSocket.bind(("0.0.0.0", self.IN_PORT))
        self.clientInputSocket, self.clientAddr = None, None

        # The frames socket.
        self.F_PORT = 1847
        self.framesSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.framesSocket.bind(("0.0.0.0", self.F_PORT))
        self.clientFramesSocket = None    
    
    def Disconnect(self):
        # The function gets nothing.
        # The function closes the sockets with the client.

        # Close sockets
        self.framesSocket.close()
        self.inputSocket.close()
    
    # Listening function:
    def WaitForClientToConnect(self):
        # The function gets nothing.
        # The function listen to the client socket to connect.

        # The input socket
        self.inputSocket.listen(1)
        print(f"Server's input socket is listening on port {self.IN_PORT}...")
        self.clientInputSocket, self.clientAddr = self.inputSocket.accept()

        # The frames socket.
        self.framesSocket.listen(1)
        print(f"Server's frames socket is listening on port {self.F_PORT}...")
        self.clientFramesSocket = self.framesSocket.accept()[0]

        print(f"The client {self.clientAddr} succssefully connected!")
        

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
    def GetKeyboardIn(self):
        # The function gets nothing.
        # The function returns the input of keyboard as a string.
        self.result = None
        def FilterOneKeyOrCombination(event):
            # The function gets nothing.
            # The functino saves the entered one single key or combination as a string in the self.result parameter.
            if event.event_type == 'down':
                if len(keyboard._pressed_events) == 1:
                    self.result = event.name
                else:
                    combo = '+'.join([keyboard.key_to_scan_codes(key)[0] for key in keyboard._pressed_events.keys()])
                    self.result = keyboard.get_hotkey_name(combo)
                keyboard.unhook_all()
                return
        
        # Attach the listener for key press events
        keyboard.on_press(FilterOneKeyOrCombination)
        
        # Wait until a key press or combination is detected
        keyboard.wait()
        return self.result
    def SendKeyboardInput(self, keyIn:str):
        # The function gets the keyboard input as a string.
        # The function sends the input to the client as a binary sequence.
        self.clientInputSocket.send("keyboard".encode())
        self.clientInputSocket.send(keyIn.encode())


    # The frames handeling
    def GetFrame(self):
        # The function gets nothing.
        # The function returns the received binary sequence, which represent a frame, from the client.
        compressedFrameBytesSize = int(self.clientFramesSocket.recv(1024).decode())
        return self.clientFramesSocket.recv(compressedFrameBytesSize)
    def DecompressImage(compressedFrame:bytes):
        # The function gets a compressed image as a byte object.
        # The function returns the given image as an Image object.
        decompressed_data = gzip.decompress(compressedFrame)
        img_stream = io.BytesIO(decompressed_data)
        return Image.open(img_stream).convert('RGB')


    def PresentFrame(newFrame:Image, width:int, height:int):
        # The function gets an Image object and the required sizes of the frames.
        # The function returns the Image object as an ImageTk object after getting resized.
        return ImageTk.PhotoImage(newFrame.resize(size=(width, height)))
        # return ImageTk.PhotoImage(newFrame)