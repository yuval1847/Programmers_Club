import customtkinter
from PIL import Image, ImageTk

class HelperFunctions:
    """A class which contain helper functions"""
    
    def CreateImage(imageFilePath, width, height):
        # The function gets a string which represent the path of the image file, the width and the height of the image.
        # The function returns a label which contain the image.
        try:
            return ImageTk.PhotoImage(Image.open(fp=imageFilePath).resize((width, height)))
        except Exception as e:
            print(e)
            return None
            
        