import customtkinter
import threading
import Pages.Base_Page
import Algo.Server_Algo

class StartPage(Pages.Base_Page.BasePage):
    """A class which represent the Start page of the program."""

    def __init__(self, master) -> None:
        super().__init__(master=master, fgColor="#031019", bgColor="#031019")

        self.server = Algo.Server_Algo.Server()

        self.currentFrame = None
        self.currentFrameLabel = customtkinter.CTkLabel(master=self,
                                                        text="")
        
        self.mutexLock = threading.Lock()
        # self.inputThread = threading.Thread(target=)
        self.framesThread = threading.Thread(target=self.Video())


    def Video(self):
        # The function gets nothing.
        # The function present the "sharescreen" from client's screen on the server's page.
        self.mutexLock.acquire()
        self.currentFrame = self.server.PresentFrame(newFrame = self.server.DecompressImage(self.server.GetFrame()), width=960, height=600)
        self.currentFrameLabel._image = self.currentFrame
        self.currentFrameLabel.place(relx=0, rely=0, anchor='center')
        self.mutexLock.release()


    def StartContolling(self):
        # The function gets nothing.
        # The function start the contolling over the client's computer
        self.framesThread.start()


    def StopControlling(self):
        # The function gets nothing.
        # The function disconects from the server.
        self.framesThread.join()
        self.server.Disconnect()