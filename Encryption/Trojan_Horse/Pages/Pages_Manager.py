import Pages.Home_Page
import customtkinter
import Pages.Server_Attack_Page

class PagesManagers(customtkinter.CTk):
    """A class which manage the pages in the program"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("960x600")
        self.resizable(False, False)
        self.configure(bg="lightpink")
        self.title("ShadowSteed 1.0")

        self.frames = {"HomePage": Pages.Home_Page.HomePage(master=self),
                       "AttackPage": Pages.Server_Attack_Page.AttackPage(master=self)}
        
        self.update_idletasks() 

        self.ShowFrame("HomePage")


    def ShowFrame(self, pageName):
        # The function gets a page name.
        # The function shows on the self the right page according to the given number.
        self.frames[pageName].pack(fill = "both", expand = True)