from PIL import Image, ImageTk
import customtkinter
import time

class StartUpPage:
    # A class which represent the starting page of the program

    def __init__(self, screen):
        self.screen = screen
        self.frame = customtkinter.CTkFrame(screen)

        self.animation = None
        self.loadingBar = customtkinter.CTkProgressBar(master=self.frame,
                                                   orientation="horizontal",
                                                   fg_color = "#81ecec",
                                                   progress_color = "#00cec9",
                                                   width = self.frame.winfo_screenwidth() - 400,
                                                   height = 10,
                                                   determinate_speed = 0.2)
        

    def LoadingAnimation(self):
        # The function gets nothing.
        # The function creating the loading animation.

        self.loadingBar.set(0)
        self.loadingBar.place(relx=0.5, rely=0.95, anchor='center')
        if self.StartAnimation() == 0:
            return 0
            
        self.screen.mainloop()

    def StartAnimation(self):
        # The function gets nothing
        # The function return 0 if the animation finished
        if self.loadingBar.get() < 1.0:
            self.loadingBar.set(self.loadingBar.get() + 0.01)
            self.frame.after(20, self.StartAnimation)
        else:
            self.loadingBar.stop()
            # Destroy frame after 5 seconds.
            self.frame.after(5000, self.frame.destroy)
            return 0


    def run(self):
        # The function gets nothing
        # The function create the enterence to the application
        
        self.frame.pack(fill="both", expand=True)
        # The big title
        lblTitle = customtkinter.CTkLabel(master=self.frame,
                                           text="STE Antivirus",
                                           font=("Inter", 100, "bold"),
                                           text_color="white",
                                           bg_color="transparent")
        lblTitle.place(relx=0.5, rely=0.45, anchor='center')


        # The sub title
        lblSubTitle = customtkinter.CTkLabel(master=self.frame,
                                              text="Safer Than Ever",
                                              font=("Inter", 25),
                                              text_color="#00cec9",
                                              bg_color="transparent")
        lblSubTitle.place(relx=0.2625, rely=0.54, anchor='center')

        # Loading label
        loadingLbl = customtkinter.CTkLabel(master=self.frame,
                                            text="Loading...",
                                            font=("Inter", 20),
                                            text_color="white",
                                            bg_color="transparent")
        loadingLbl.place(relx=0.09, rely=0.9, anchor="center")

        # The animation
        if self.LoadingAnimation() == 0:
            return 0

        self.screen.mainloop()