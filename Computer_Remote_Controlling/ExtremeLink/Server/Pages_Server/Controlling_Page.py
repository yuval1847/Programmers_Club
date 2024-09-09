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

        # Threads and mutex lock.
        self.mutexLock = threading.Lock()
        # self.inputThread = threading.Thread(target=)
        self.framesThread = threading.Thread(target=self.PresentVideo)

        # Load default frame:
        self.LoadDefaultFrame()

        # Play and Stop buttons:
        self.playButton = customtkinter.CTkButton(master=self,
                                                  text="",
                                                  command=self.Start,
                                                  image=tkinter.PhotoImage(file=os.getcwd()+"\\Img\\play_icon.png"))
        self.playButton.place(relx=0.4, rely=0.95, anchor='center')
        
        self.pauseButton = customtkinter.CTkButton(master=self,
                                                  text="",
                                                  command=self.Pause,
                                                  image=tkinter.PhotoImage(file=os.getcwd()+"\\Img\\pause_icon.png"))
        self.pauseButton.place(relx=0.6, rely=0.95, anchor='center')




    def Start(self):
        # The function gets nothing.
        # The function start the streaming and the controlling over the client's computer.
        self.master.server.Start()
        self.StartViewStream()
        self.StartControlling()
    def Pause(self):
        # The function gets nothing.
        # The function pause the streaming and the controlling over the client's computer.
        self.master.server.Pause()
        self.StopViewStream()
        self.StopControlling()
        self.LoadDefaultFrame()


    # Frames:
    def StartViewStream(self):
        # The function gets nothing.
        # The function start the thread of the frames stream.
        self.framesThread.start()
    def StopViewStream(self):
        # The function gets nothing.
        # The function stop the thread of the frames stream.
        self.framesThread.join()
    def PresentVideo(self):
        # The function gets nothing.
        # The function present the "sharescreen" from client's screen on the server's controlling page.
        self.mutexLock.acquire()
        self.currentFrame = self.master.server.PresentFrame(newFrame = self.master.server.DecompressImage(self.master.server.GetFrame()), width=960, height=540)
        self.currentFrameLabel._image = self.currentFrame
        self.currentFrameLabel.place(relx=0, rely=0, anchor='center')
        self.mutexLock.release()
    def LoadDefaultFrame(self):
        # The function gets nothing.
        # The function loads the default frame on the screen.
        image_path = os.path.join(os.getcwd(), "Img", "default_frame.png")
        self.currentFrame = customtkinter.CTkImage(light_image=PIL.Image.open(image_path), size=(960, 540))
        
        self.currentFrameLabel = customtkinter.CTkLabel(master=self,
                                                        text="",
                                                        image=self.currentFrame)
        
        # Positioning the label correctly with relative positioning.
        self.currentFrameLabel.place(relx=0.5, rely=0.45, anchor='center')


    # Input:
    def StartControlling(self):
        # The function gets nothing.
        # The function start the contolling over the client's computer
        pass
        # self.inputThread.start()

    def StopControlling(self):
        # The function gets nothing.
        # The function disconects from the server.
        pass
        # self.inputThread.join()