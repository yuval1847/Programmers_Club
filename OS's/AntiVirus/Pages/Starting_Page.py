from PIL import Image, ImageTk
import customtkinter
import time
import Pages.Scanning_Page


class StartUpPage:
    # A class which represent the starting page of the program

    def __init__(self):
        self.screen = customtkinter.CTk()
        self.screen.geometry("960x600")
        self.screen.resizable(False, False)
        self.screen.title("STE Antivirus")
        # Init the grid of the screen
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_rowconfigure(0, weight=1)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.frame = customtkinter.CTkFrame(self.screen)
        self.loadingBar = customtkinter.CTkProgressBar(master=self.frame,
                                                   orientation="horizontal",
                                                   fg_color = "#16a085",
                                                   progress_color = "#00cec9",
                                                   width = self.frame.winfo_screenwidth() - 400,
                                                   height = 10,
                                                   determinate_speed = 0.2)
        
    def LoadingAnimation(self):
        # The function gets nothing.
        # The function creating the loading animation.
        self.loadingBar.set(0)
        self.loadingBar.place(relx=0.5, rely=0.95, anchor='center')
        self.StartAnimation()
        self.screen.update()

    def StartAnimation(self):
        # The function gets nothing.
        # The function start the loading animation of the loading progresss bar.

        def UpdateLoadingBar():
            # A recursive function using update_idletasks to make the update proccess continue while moving the
            # program screen on the computer screen.
            if self.loadingBar.get() < 1.0:
                self.loadingBar.set(self.loadingBar.get() + 0.01)
                self.frame.after(40, UpdateLoadingBar)  # Schedule the next update
                self.screen.update_idletasks()  # Process pending GUI events
            else:
                self.loadingBar.stop()
                self.frame.destroy()
                self.frame.after(2000)
                
                Pages.Scanning_Page.ScanningPage(self.screen).run()
        UpdateLoadingBar()


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
        self.LoadingAnimation()

        self.screen.mainloop()