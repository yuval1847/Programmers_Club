import customtkinter

class ScanningPage:
    # A class which represent the scanning page.

    def __init__(self, screen) -> None:
        self.screen = screen
        self.frame = customtkinter.CTkFrame(screen)
        self.isFinishedScanning = False
        
    def run(self):
        
        self.frame.pack(fill="both", expand=True)
        lblTitle = customtkinter.CTkLabel(master=self.frame,
                                           text="Scanning Mode",
                                           font=("Inter", 30, "bold"),
                                           text_color="white",
                                           bg_color="transparent")
        lblTitle.place(relx=0.5, rely=0.1, anchor="center")

        startButton = customtkinter.CTkButton(master=self.frame,
                                              text="Start Scan",
                                              font=("Inter", 15),
                                              text_color="white",
                                              bg_color="transparent",
                                              corner_radius=10)
        startButton.configure(fg_color="#00cec9")
        startButton.place(relx=0.5, rely=0.8, anchor="center")

        if self.isFinishedScanning:
            return 0

        self.screen.mainloop()