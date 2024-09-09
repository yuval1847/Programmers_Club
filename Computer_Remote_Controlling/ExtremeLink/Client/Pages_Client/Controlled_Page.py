import customtkinter
import Pages_Client.Base_Page

class ControlledPage(Pages_Client.Base_Page.BasePage):
    """A class which represent the controlled page."""

    def __init__(self, master):
        super().__init__(master=master, fgColor="#00cec9", bgColor="#00cec9")
        self.master = master

        customtkinter.CTkLabel(master=self,
                               text="The Server is Controling Now!",
                               font=("Inter", 70, "bold"),
                               text_color="#031019",
                               bg_color="transparent").place(relx=0.5, rely=0.2, anchor='center')