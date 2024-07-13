import customtkinter
import Pages.Base_Page
import Pages.Helper_Functions
import Algo.Server

class AttackPage(Pages.Base_Page.BasePage):
    """A class which represent the attack page from the server side."""

    def __init__(self, master) -> None:
        super().__init__(master=master, fgColor="#031019", bgColor="#031019")
        self.serverIconLabel = customtkinter.CTkLabel(master=self,
                                                    text="",
                                                    image=Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\Server.png", width=200, height=200))
        self.serverIconLabel.place(relx=0.2, rely=0.465, anchor='center')

        self.victimIconLabel = customtkinter.CTkLabel(master=self,
                                                    text="",
                                                    image=Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\Victim.png", width=200, height=200))
        self.victimIconLabel.place(relx=0.8, rely=0.465, anchor='center')

        self.dots = [customtkinter.CTkLabel(master=self, text="", image=Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\emptyDot.png", width=30, height=30)) for i in range(5)]
        self.animation_running = True
        self.ConnectingDotsAnimation()
       
    def ConnectingDotsAnimation(self):
        # The function places the animation dots on the frame according to the animation itself.
        self.after(0, self.animate_dots)

    def animate_dots(self):
        if self.animation_running:
            for i in range(5):
                if i % 5 == i:
                    dot_image = Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\filledDot.png", width=30, height=30)
                else:
                    dot_image = Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\emptyDot.png", width=30, height=30)

                dot_label = customtkinter.CTkLabel(master=self, text="", image=dot_image)
                dot_label.place(relx=((10 - i) / 10) - 0.3, rely=0.55, anchor='center')
                self.dots.append(dot_label)
            self.after(500, self.animate_dots)
        else:
            for dot in self.dots:
                dot.destroy()

    def StartServer(self):
        # The function gets nothing.
        # The function creates a server instance and starts it.
        server = Algo.Server.Server()
        if server.send_secret_key_to_client():
            self.animation_running = False
        return -1
