import tkinter
import customtkinter
import awesometkinter
import Files_Enumeration
import Scanning_Files_For_Viruses
import Pages.Results_Page

class ScanningPage:
    # A class which represent the scanning page.

    def __init__(self, screen) -> None:
        self.screen = screen
        self.frame = customtkinter.CTkFrame(self.screen)
        self.isFinishedScanning = False
        self.folderToScan = ""
        self.listOfFiles = []
            
    def Scanning(self):
        # The function gets 
        # The function create the progress bar of the scanning progress and call the scanning proccess functions

        # Open a directory selection dialog and store the selected directory
        self.folderToScan = tkinter.filedialog.askdirectory()
        if not self.folderToScan:
            # Inform the user that no directory was selected
            tkinter.messagebox.showerror("Error", "No folder selected") 

        else:
            # Enumerate all the files in the given path.
            self.listOfFiles = Files_Enumeration.FilesEnumeration(self.folderToScan)
            print(self.listOfFiles)
            # Check if there is no files in the folder
            if len(self.listOfFiles) == 0:
                self.StartAnimation(100)
                return 0
            else:
                self.StartAnimation(100/len(self.listOfFiles))
                return 0
                
    def StartAnimation(self, scanningRate):
        # The function gets 
        # The function return 0 if the animation finished
        listOfInfectedFiles = []
        isThereVirus = False
        for i in range(len(self.listOfFiles)):
            print(self.listOfFiles[i])
            self.scanningBar.set(self.scanningBar.get() + scanningRate)
            if Scanning_Files_For_Viruses.IsFileClear(self.listOfFiles[i], self.screen):
                print(f"{self.listOfFiles[i]} - Clear")
            else:
                print(f"{self.listOfFiles[i]} - Suspected or Infected")    
                listOfInfectedFiles.append(self.listOfFiles[i])  
                isThereVirus = True          
            self.screen.update()
            
        self.scanningBar.stop()
        self.frame.destroy()
        self.frame.after(2000)
        Pages.Results_Page.Results(self.screen, isThereVirus, listOfInfectedFiles).run()
        isFinishedScanning = True

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

        self.scanningBar = awesometkinter.RadialProgressbar(self.frame,
                                                       fg='#00cec9',
                                                       parent_bg="#2a2d2e",
                                                       size=(400, 400))
        self.scanningBar.place(relx=0.5, rely=0.5, anchor="center")

        startButton = customtkinter.CTkButton(master=self.frame,
                                              text="Start Scan",
                                              font=("Inter", 15, "bold"),
                                              text_color="white",
                                              bg_color="#2a2d2e",
                                              fg_color="#00cec9",
                                              corner_radius=10,
                                              command=self.Scanning)
        startButton.place(relx=0.5, rely=0.85, anchor="center")

        if self.isFinishedScanning:
            return 0

        self.screen.mainloop()