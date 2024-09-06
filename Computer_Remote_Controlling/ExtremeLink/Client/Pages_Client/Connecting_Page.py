import Pages_Client.Base_Page
import Algo_Client.Client_Algo
import customtkinter
import tkinter
import threading
import os

class ConnectingPage(Pages_Client.Base_Page.BasePage):
    """A class which represent the connecting page."""

    def __init__(self, master):
        super().__init__(master=master, fgColor="#00cec9", bgColor="#00cec9")
        self.master = master
        self.StartUpUIElementsPack()


    def StartUpUIElementsPack(self):
        # The function gets nothing
        # The function load all the UI elements on the page's frame master itself.
        self.EraseUIElements()

        customtkinter.CTkLabel(master=self,
                               text="Choose",
                               font=("Inter", 70, "bold"),
                               text_color="#031019",
                               bg_color="transparent").place(relx=0.5, rely=0.2, anchor='center')
        
        customtkinter.CTkLabel(master=self,
                               text="Here you can choose your connection type. If you doesn't sure which\none to choose find more info about it: https://www.techtarget.com/\nsearchnetworking/feature/Whats-the-difference-between-internet-and-Ethernet",
                               font=("Inter", 18, "bold"),
                               text_color="#031019",
                               bg_color="transparent").place(relx=0.5, rely=0.35, anchor='center')


        # Play and Stop buttons:

        localNetworkBtn = customtkinter.CTkButton(master=self,
                                                  text="Local-Network",
                                                  font=("Inter", 16, "bold"),
                                                  text_color="#00cec9",
                                                  fg_color="#031019",
                                                  bg_color="#2a2d2e",
                                                  corner_radius=0,
                                                  width=150,
                                                  height=45,
                                                  image=tkinter.PhotoImage(file=os.getcwd()+"\\Client\\Img\\local_network_icon.png"),
                                                  command=self.LocalNetworkChoice)
        localNetworkBtn.place(relx=0.6, rely=0.55, anchor='center')

        internetBtn = customtkinter.CTkButton(master=self,
                                              text="Internet",
                                              font=("Inter", 16, "bold"),
                                              text_color="#00cec9",
                                              fg_color="#031019",
                                              bg_color="#2a2d2e",
                                              corner_radius=0,
                                              width=125,
                                              height=45,
                                              image=tkinter.PhotoImage(file=os.getcwd()+"\\Client\\Img\\internet_icon.png"),
                                              command=self.InternetChoice)
        internetBtn.place(relx=0.4, rely=0.55, anchor='center')


    def LocalNetworkChoice(self):
        # The function gets nothing.
        # The function creates the server and load the controlling page.
        
        pass


    def InternetChoice(self):
        # The function gets nothing.
        # The function load the UI elements of the page an earase the former ones.
        
        pass


    def WaitingForClientConnectionUI(self):
        # The function gets nothing.
        # The function creates the server and loads the UI elements while waiting for the client connection.
        self.EraseUIElements()

        customtkinter.CTkLabel(master=self,
                                text="Connected!",
                                font=("Inter", 70, "bold"),
                                text_color="#031019",
                                bg_color="transparent").place(relx=0.5, rely=0.2, anchor='center')
        customtkinter.CTkLabel(master=self,
                                text="You are sharing your screen to the server right now.",
                                font=("Inter", 18, "bold"),
                                text_color="#031019",
                                bg_color="transparent").place(relx=0.5, rely=0.4, anchor='center')