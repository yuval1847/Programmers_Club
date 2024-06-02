import customtkinter

class Results:
    # A class which represent a page of the results of the scanning.

    def __init__(self, screen, isThereVirus, listOfVirusFiles) -> None:
        self.screen = screen
        self.frame = customtkinter.CTkFrame(self.screen)
        self.isThereVirus = isThereVirus
        self.listOfVirusFiles = listOfVirusFiles

    def run(self):
        lblTitle = customtkinter.CTkLabel(master=self.frame,
                                           text="Scanning Results",
                                           font=("Inter", 40, "bold"),
                                           text_color="white",
                                           bg_color="transparent")
        lblTitle.place(relx=0.5, rely=0.1, anchor='center')

        label = customtkinter.CTkLabel(master=self.frame,
                                        font=("Inter", 20, "bold"),
                                        text_color="#00cec9",
                                        bg_color="transparent")
        label._text = "No Virus Detected!"
        if self.isThereVirus:
            for filePath in self.listOfVirusFiles:
                label._text += f"\n{filePath}"
            label.place(relx=0.15, rely=0.15, anchor="center")

        else:
            label._text = "No virus detected!"
            label.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.pack(fill="both", expand=True)
        self.screen.mainloop()