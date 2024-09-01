import customtkinter
import Pages_Client.Start_Page

class PagesManager(customtkinter.CTk):
    """A class which manage the pages in the program"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("960x600")
        self.resizable(False, False)
        self.configure(bg="gray24")
        self.title("ExtremeLink v1.0 Server")

        self.frames = {"StartPage": Pages_Client.Start_Page.StartPage(master=self)}  
             
        self.update_idletasks() 

        self.ShowFrame("StartPage")


    def ShowFrame(self, pageName):
        # The function gets a page name.
        # The function shows on the self the right page according to the given number.
        self.frames[pageName].pack(fill = "both", expand = True)