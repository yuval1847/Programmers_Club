import Pages.Scanning_Page
import Pages.Starting_Page
import customtkinter
import time

class ScreensManager:
    # A class which manage the pages of the game.

    def __init__(self) -> None:
        self.screen = customtkinter.CTk()
        self.screen.geometry("960x600")
        self.screen.resizable(False, False)

        # Configure the grid for centering
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_rowconfigure(0, weight=1)

        # Set the program to be on dark mode.
        customtkinter.set_appearance_mode("dark")

        # Sets the color of the widgets.
        customtkinter.set_default_color_theme("dark-blue")

        #self.startUpPage = Pages.Starting_Page.StartUpPage(self.screen)
        self.scanningPage = Pages.Scanning_Page.ScanningPage(self.screen)
        self.pages = [#self.startUpPage,
                      self.scanningPage
                      ]
        
        self.currentPage = self.pages[0]

    def ChangeCurrentPage(self, index):
        # The function gets an index
        # The fucntion changes the current page to the page which in the index of the list of pages.
        self.currentPage = self.pages[index]

    def RunCurrentPage(self):
        # The function gets nothing.
        # The fucntion run the current page function.
        self.currentPage.run()