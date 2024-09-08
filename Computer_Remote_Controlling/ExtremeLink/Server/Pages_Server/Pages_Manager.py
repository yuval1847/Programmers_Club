import customtkinter
import Algo_Server.Server_Class
import Pages_Server.Base_Page
import Pages_Server.Pages_Manager
import Pages_Server.Start_Page
import Pages_Server.Connecting_Page
import Pages_Server.Controlling_Page

class PagesManager(customtkinter.CTk):
    """A class which manage the pages in the program"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("960x600")
        self.resizable(False, False)
        self.configure(bg="gray24")
        self.title("ExtremeLink v1.0 Server")

        # The instance of the server object.
        self.server = Algo_Server.Server_Class.Server()

        self.frames = {"StartPage": Pages_Server.Start_Page.StartPage(master=self),
                       "ConnectingPage": Pages_Server.Connecting_Page.ConnectingPage(master=self),
                       "ControllingPage": Pages_Server.Controlling_Page.ControllingPage(master=self)}  
                
             
        self.update_idletasks()

        self.ShowFrame("StartPage")
        #self.ShowFrame("ConnectingPage")


    def ShowFrame(self, pageName):
        # The function gets a page name.
        # The function shows on the self the right page according to the given number.
        self.frames[pageName].pack(fill = "both", expand = True)