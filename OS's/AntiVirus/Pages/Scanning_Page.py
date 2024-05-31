import customtkinter
import awesometkinter

class ScanningPage:
    # A class which represent the scanning page.

    def __init__(self, screen) -> None:
        self.screen = screen
        self.frame = customtkinter.CTkFrame(screen)
        self.isFinishedScanning = False
        
    def Scanning(self):
        # The function gets nothing
        # The function create the progress bar of the scanning progress and call the scanning proccess functions
        scanningBar = awesometkinter.RadialProgressbar(self.frame,
                                                       fg='green',
                                                       parent_bg="#2a2d2e",
                                                       size=(400, 400))
        scanningBar.place(relx=0.5, rely=0.5, anchor="center")
        self.screen.mainloop()

    def run(self):
        

        backgroundCanvas = customtkinter.CTkCanvas(master=self.frame,
                                                   bg="#2a2d2e",
                                                   width=1300,
                                                   height=800,
                                                   highlightthickness=0)
        backgroundCanvas.place(relx=0.5, rely=0.5, anchor="center")

        self.frame.pack(fill="both", expand=True)
        lblTitle = customtkinter.CTkLabel(master=self.frame,
                                           text="Scanning Mode",
                                           font=("Inter", 30, "bold"),
                                           text_color="white",
                                           bg_color="#2a2d2e")
        lblTitle.place(relx=0.5, rely=0.1, anchor="center")

        startButton = customtkinter.CTkButton(master=self.frame,
                                              text="Start Scan",
                                              font=("Inter", 15, "bold"),
                                              text_color="white",
                                              bg_color="#2a2d2e",
                                              corner_radius=10,)
        startButton.configure(fg_color="#00cec9")
        startButton.place(relx=0.5, rely=0.85, anchor="center")

        self.Scanning()

        if self.isFinishedScanning:
            return 0

        self.screen.mainloop()