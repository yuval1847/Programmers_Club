import customtkinter
import Pages_Server.Base_Page

class StartPage(Pages_Server.Base_Page.BasePage):
    """A class which represent the Start page of the program."""

    def __init__(self, master) -> None:
        super().__init__(master=master, fgColor="#031019", bgColor="#031019")

        # Customize loading bar
        self.loadingBar = customtkinter.CTkProgressBar(master=self,
                                                   orientation="horizontal",
                                                   fg_color = "#16a085",
                                                   progress_color = "#00cec9",
                                                   width = 900,
                                                   height = 10)
        self.loadingBar.place(relx=0.5, rely=0.95, anchor='center')
        
        # Customize the Title and the icon
        self.lblTitle = customtkinter.CTkLabel(master=self,
                                           text="ExtremLink - Server",
                                           font=("Inter", 85, "bold"),
                                           text_color="#00cec9",
                                           bg_color="transparent")
        self.lblTitle.place(relx=0.5, rely=0.465, anchor='center')

        self.lblSubTitle = customtkinter.CTkLabel(master=self,
                                              text="Triple C - Choose, Connect, Control.",
                                              font=("Inter", 25),
                                              text_color="#00cec9",
                                              bg_color="transparent")
        self.lblSubTitle.place(relx=0.3, rely=0.565, anchor='center')

        self.loadingLabel = customtkinter.CTkLabel(master=self,
                                                   text="Loading...",
                                                   font=("Inter", 18),
                                                   text_color="#00cec9",
                                                   bg_color="transparent")
        self.loadingLabel.place(relx=0.075, rely=0.9, anchor='center')

        self.LoadingBarAnimation()


    def LoadingBarAnimation(self):
        # The function gets nothing.
        # The function creats the loading animation.
        self.loadingBar.set(0)
        self.StartAnimation()

    def StartAnimation(self):
        # The function gets nothing.
        # The function start the loading animation of the loading progresss bar.
        def UpdateLoadingBar():
            # A recursive function using update_idletasks to make the update proccess continue while moving the
            # program screen on the computer screen.
            if self.loadingBar.get() < 1.0:
                self.loadingBar.set(self.loadingBar.get() + 0.005)
                self.after(40, UpdateLoadingBar)  # Schedule the next update
            else:
                self.loadingBar.stop()
                self.destroy()
                self.after(1, lambda: self.master.ShowFrame("ConnectingPage"))
        UpdateLoadingBar()