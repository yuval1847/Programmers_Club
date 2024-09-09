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
        self.isAllSettingsRight = False
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
        self.LoadLocalNetworkChoiceUI()


    def InternetChoice(self):
        # The function gets nothing.
        # The function load the UI elements of the page an earase the former ones.     
        pass


    def LoadLocalNetworkChoiceUI(self):
        # The function gets nothing.
        # The function load the local network choice ui.
        self.EraseUIElements()

        self.lblTitle = customtkinter.CTkLabel(master=self,
                                           text="Connection Settings",
                                           font=("Inter", 70, "bold"),
                                           text_color="#031019",
                                           bg_color="transparent")
        self.lblTitle.place(relx=0.5, rely=0.1, anchor='center')


        # Getting server's ip
        customtkinter.CTkLabel(master=self,
                               text="Server's IP:",
                               font=("Inter", 18, "bold"),
                               text_color="#031019",
                               bg_color="transparent").place(relx=0.43, rely=0.4, anchor='center')
        
        self.serverIpEntry = customtkinter.CTkEntry(master=self,
                                                     font=("Inter", 18, "bold"),
                                                     placeholder_text="X.X.X.X",
                                                     width = 150)
        self.serverIpEntry.place(relx=0.57, rely=0.4, anchor='center')
        

        saveAndConnectBtn = customtkinter.CTkButton(master=self,
                                              text="Save & Connect",
                                              font=("Inter", 16, "bold"),
                                              text_color="#00cec9",
                                              fg_color="#031019",
                                              bg_color="#2a2d2e",
                                              corner_radius=0,
                                              width=125,
                                              height=45,
                                              image=tkinter.PhotoImage(file=os.getcwd()+"\\Client\\Img\\connection_icon.png"),
                                              command=self.CheckEnteredSettings)
        saveAndConnectBtn.place(relx=0.5, rely=0.9, anchor='center')

        if self.isAllSettingsRight == True:
            self.master.client = Algo_Client.Client_Algo.Client(serverAddr=self.serverIpEntry.get())
            self.master.ShowFrame("")
        

    def CheckEnteredSettings(self):
        # The function gets nothing.
        # The function checks the entered settings.
        
        # Checking the server ip:
        splitedIp = self.serverIpEntry.get().split(".")
        if len(splitedIp) != 4:
            self.LoadErrorIpTyping()
            return
        try:
            for field in splitedIp:
                if int(field) < 1 or int(field) > 255:
                    self.LoadErrorIpTyping()
                    return
        except Exception:
            self.LoadErrorIpTyping()
            return
        
        print("The ip is okay")

        self.isAllSettingsRight = True


    def LoadErrorIpTyping(self):
        # The function gets nothing.
        # The function load an error massesage if the entered ip doesn't follow the IPv4 protocol.
        customtkinter.CTkLabel(master=self,
                               text="The entered ip doesn't follow the tcp/ip protocol rules!",
                               font=("Inter", 17, "bold"),
                               text_color="#e74c3c",
                               bg_color="transparent").place(relx=0.5, rely=0.8, anchor='center')
        
        customtkinter.CTkLabel(master=self,
                               text="",
                               image=tkinter.PhotoImage(file=os.getcwd()+"\\Client\\Img\\error_icon.png"),
                               bg_color="transparent").place(relx=0.25, rely=0.8, anchor='center')
        #image=tkinter.PhotoImage(file=os.getcwd()+"\\Client\\Img\\error_icon.png")
