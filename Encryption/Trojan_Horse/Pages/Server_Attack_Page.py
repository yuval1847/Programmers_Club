import customtkinter
import Pages.Base_Page
import Pages.Helper_Functions
import Algo.Server
import threading

class AttackPage(Pages.Base_Page.BasePage):
    """A class which represents the attack page from the server side."""

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

        self.dot_labels = []
        self.dots = [Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\filledDot.png", width=30, height=30),
                     Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\emptyDot.png", width=30, height=30),
                     Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\emptyDot.png", width=30, height=30),
                     Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\emptyDot.png", width=30, height=30),
                     Pages.Helper_Functions.HelperFunctions.CreateImage(imageFilePath="Images\\emptyDot.png", width=30, height=30)]
        
        self.animation_running = True
        self.dotsAnimationThread = threading.Thread(target=self.ConnectingDotsAnimation)
        self.dotsAnimationThread.start()

        self.startServerThread = threading.Thread(target=self.StartServer)
        self.startServerThread.start()

    def ConnectingDotsAnimation(self):
        if self.animation_running:
            for label in self.dot_labels:
                label.destroy()

            self.dot_labels = []
            for i in range(5):
                dot_label = customtkinter.CTkLabel(master=self, text="", image=self.dots[i])
                dot_label.place(relx=((10 - i) / 10) - 0.3, rely=0.55, anchor='center')
                self.dot_labels.append(dot_label)
            
            self.dots = [self.dots[1]] + self.dots[2:] + [self.dots[0]]
            self.after(500, self.ConnectingDotsAnimation)  # Schedule the next call

    def StartServer(self):
        # The function gets nothing.
        # The function creates a server instance and starts it.
        server = Algo.Server.Server()
        if server.SendSecretKeyToClient():
            self.animation_running = False
            self.dotsAnimationThread.join()
        self.startServerThread.join()
        return -1
