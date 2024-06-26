import Pages.Scanning_Page
import Pages.Starting_Page
import customtkinter
import os

class ScreensManager:
    # A class which manage the pages of the game.

    def __init__(self) -> None:
        self.screen = customtkinter.CTk()
        self.screen.geometry("960x600")
        self.screen.resizable(False, False)
        self.screen.title("STE Antivirus")
        # Init the grid of the screen
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_rowconfigure(0, weight=1)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.pages = [Pages.Starting_Page.StartUpPage(self.screen).run(),
                      Pages.Scanning_Page.ScanningPage(self.screen).run()]