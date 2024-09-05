import customtkinter
import tkinter
import threading
import PIL
import os
import Pages_Server.Base_Page
import Algo_Server.Server_Class

class ControllingPage(Pages_Server.Base_Page.BasePage):
    """A class which represent the controlling page of the program."""

    def __init__(self, master) -> None:
        super().__init__(master=master, fgColor="#031019", bgColor="#031019")
        self.master = master
        self.isRunning = True

        self.currentFrame = None
        self.currentFrameLabel = None

        # Load default frame:
        self.LoadDefaultFrame()

        
        # Control
        # customtkinter.CTkLabel(master=self,
        #                        text="Control!",
        #                        font=("Inter", 70, "bold"),
        #                        text_color="#00cec9",
        #                        bg_color="transparent").place(relx=0.5, rely=0.1, anchor='center')

        # Play and Stop buttons:
        self.playButton = customtkinter.CTkButton(master=self,
                                                  text="",
                                                  image=tkinter.PhotoImage(file=os.getcwd()+"\\Server\\Img\\play_icon.png"))
        self.playButton.place(relx=0.4, rely=0.95, anchor='center')
        
        self.stopButton = customtkinter.CTkButton(master=self,
                                                  text="",
                                                  image=tkinter.PhotoImage(file=os.getcwd()+"\\Server\\Img\\pause_icon.png"))
        self.stopButton.place(relx=0.6, rely=0.95, anchor='center')




        # Threads and mutex lock.
        self.mutexLock = threading.Lock()
        # self.inputThread = threading.Thread(target=)
        self.framesThread = threading.Thread(target=self.Video())


        # Operate the page's functions:
        while True:
            while self.isRunning:
                self.Video()
            while not self.isRunning:
                pass


    def LoadDefaultFrame(self):
        # The function gets nothing.
        # The function loads the default frame on the screen.
        image_path = os.path.join(os.getcwd(), "Server", "Img", "default_frame.png")
        self.currentFrame = customtkinter.CTkImage(light_image=PIL.Image.open(image_path), size=(960, 540))
        
        self.currentFrameLabel = customtkinter.CTkLabel(master=self,
                                                        text="",
                                                        image=self.currentFrame)
        
        # Positioning the label correctly with relative positioning.
        self.currentFrameLabel.place(relx=0.5, rely=0.45, anchor='center')

    
    def Video(self):
        # The function gets nothing.
        # The function present the "sharescreen" from client's screen on the server's page.
        self.mutexLock.acquire()
        self.currentFrame = self.server.PresentFrame(newFrame = self.server.DecompressImage(self.server.GetFrame()), width=960, height=540)
        self.currentFrameLabel._image = self.currentFrame
        self.currentFrameLabel.place(relx=0, rely=0, anchor='center')
        self.mutexLock.release()


    def StartControlling(self):
        # The function gets nothing.
        # The function start the contolling over the client's computer
        if self.isRunning:
            return
        self.isRunning = True
        self.framesThread.start()


    def StopControlling(self):
        # The function gets nothing.
        # The function disconects from the server.
        if not self.isRunning:
            return
        self.isRunning = False
        self.framesThread.join()
        # Write in the server class an additional function of pause
        #self.master.server.Disconnect()