import customtkinter

class BasePage(customtkinter.CTkFrame):
    """A class which represent the home page of the program."""

    def __init__(self, master, fgColor, bgColor) -> None:
        super().__init__(master=master, fg_color=fgColor, bg_color=bgColor)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)