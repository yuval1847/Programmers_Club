import Pages_Server.Base_Page
import Algo_Server.Server_Class
import customtkinter
import tkinter
import threading
import os

class ConnectingPage(Pages_Server.Base_Page.BasePage):
    """A class which represent the connecting page."""

    def __init__(self, master):
        super().__init__(master=master, fgColor="#031019", bgColor="#031019")
        self.master = master
        self.StartUpUIElementsPack()


    def StartUpUIElementsPack(self):
        # The function gets nothing
        # The function load all the UI elements on the page's frame master itself.
        self.EraseUIElements()

        customtkinter.CTkLabel(master=self,
                               text="Choose",
                               font=("Inter", 70, "bold"),
                               text_color="#00cec9",
                               bg_color="transparent").place(relx=0.5, rely=0.2, anchor='center')
        
        customtkinter.CTkLabel(master=self,
                               text="Here you can choose your connection type. If you doesn't sure which\none to choose find more info about it: https://www.techtarget.com/\nsearchnetworking/feature/Whats-the-difference-between-internet-and-Ethernet",
                               font=("Inter", 18, "bold"),
                               text_color="#00cec9",
                               bg_color="transparent").place(relx=0.5, rely=0.35, anchor='center')


        # Play and Stop buttons:

        localNetworkBtn = customtkinter.CTkButton(master=self,
                                                  text="Local-Network",
                                                  font=("Inter", 16, "bold"),
                                                  text_color="#031019",
                                                  fg_color="#00cec9",
                                                  bg_color="#2a2d2e",
                                                  corner_radius=0,
                                                  width=150,
                                                  height=45,
                                                  image=tkinter.PhotoImage(file=os.getcwd()+"\\Server\\Img\\local_network_icon.png"),
                                                  command=self.LocalNetworkChoice)
        localNetworkBtn.place(relx=0.6, rely=0.55, anchor='center')

        internetBtn = customtkinter.CTkButton(master=self,
                                              text="Internet",
                                              font=("Inter", 16, "bold"),
                                              text_color="#031019",
                                              fg_color="#00cec9",
                                              bg_color="#2a2d2e",
                                              corner_radius=0,
                                              width=125,
                                              height=45,
                                              image=tkinter.PhotoImage(file=os.getcwd()+"\\Server\\Img\\internet_icon.png"),
                                              command=self.InternetChoice)
        internetBtn.place(relx=0.4, rely=0.55, anchor='center')


    def LocalNetworkChoice(self):
        # The function gets nothing.
        # The function creates the server and load the controlling page.
        
        def WaitForConnection():
            self.master.server = Algo_Server.Server_Class.Server()
            self.master.server.WaitForClientToConnect()
            self.master.ShowFrame("ControllingPage")
            self.destroy()
        
        threading.Thread(target=WaitForConnection).start()

        self.WaitingForClientConnectionUI()


    def InternetChoice(self):
        # The function gets nothing.
        # The function load the UI elements of the page an earase the former ones.
        
        pass


    def WaitingForClientConnectionUI(self):
        # The function gets nothing.
        # The function creates the server and loads the UI elements while waiting for the client connection.
        self.EraseUIElements()

        customtkinter.CTkLabel(master=self,
                                text="Connect",
                                font=("Inter", 70, "bold"),
                                text_color="#00cec9",
                                bg_color="transparent").place(relx=0.5, rely=0.2, anchor='center')

        self.lbl = customtkinter.CTkLabel(master=self,
                                        text="Waiting for client connection",
                                        font=("Inter", 18, "bold"),
                                        text_color="#00cec9",
                                        bg_color="transparent")
        self.lbl.place(relx=0.5, rely=0.85, anchor='center')

        def update_label():
            current_text = self.lbl.cget("text")
            if current_text.endswith("..."):
                self.lbl.configure(text="Waiting for client connection")
            else:
                self.lbl.configure(text=current_text + ".")
            self.after(500, update_label)

        update_label()