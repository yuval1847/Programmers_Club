import Pages_Server.Base_Page
import customtkinter
import tkinter
import os

class ConnectingPage(Pages_Server.Base_Page.BasePage):
    """A class which represent the connecting page."""

    def __init__(self, master):
        super().__init__(master=master, fgColor="#031019", bgColor="#031019")

        self.StartUpUIElementsPack()
    

    def EraseUIElements(self):
        # The function gets nothing.
        # The function erase all the UI elements on the frame.
        for widget in self.winfo_children():
            widget.destroy()

    
    def StartUpUIElementsPack(self):
        # The function gets nothing
        # The function load all the UI elements on the page's frame master itself.
        self.EraseUIElements()

        customtkinter.CTkLabel(master=self,
                               text="Choose & Connect",
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
                                                  command=self.LocalNetworkSettingsUIElementsPack)
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
                                              command=self.InternetSettingsUIElementsPack)
        internetBtn.place(relx=0.4, rely=0.55, anchor='center')


    def LocalNetworkSettingsUIElementsPack(self):
        # The function gets nothing.
        # The function load the UI elements of the page an earase the former ones.
        pass


    def InternetSettingsUIElementsPack(self):
        # The function gets nothing.
        # The function load the UI elements of the page an earase the former ones.
        
        pass