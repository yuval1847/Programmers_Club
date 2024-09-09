import customtkinter
import Algo_Client.Client_Algo
import Pages_Client.Start_Page
import Pages_Client.Connecting_Page
import Pages_Client.Controlled_Page


class PagesManager(customtkinter.CTk):
    """A class which manage the pages in the program"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("960x600")
        self.resizable(False, False)
        self.configure(bg="gray24")
        self.title("ExtremeLink v1.0 Server")

        self.client = None

        self.frames = {"StartPage": Pages_Client.Start_Page.StartPage(master=self),
                       "ConnectingPage": Pages_Client.Connecting_Page.ConnectingPage(master=self),
                       "ControlledPage": Pages_Client.Controlled_Page.ControlledPage(master=self)}  
            
        self.update_idletasks() 

        self.ShowFrame("StartPage")


    def ShowFrame(self, pageName):
        # The function gets a page name.
        # The function shows on the self the right page according to the given number.
        self.frames[pageName].pack(fill = "both", expand = True)
