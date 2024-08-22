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
                    self.result = keyboard.get_hotkey_name(combo)  # Store the combination as a result
                
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
