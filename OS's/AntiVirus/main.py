import Pages.GuiManager as GuiManager

def main():
    # # The main function
    # folderToScan = input("Enter a folder to scan: ")

    # # Enumerate all the files in the given path.
    # listOfFiles = Files_Enumeration.FilesEnumeration(folderToScan)
    
    # # Scan any files and print the results.
    # for filePath in listOfFiles:
    #     if Scanning_Files_For_Viruses.IsFileClear(filePath):
    #         print(f"{filePath} - Clear")
    #     else:
    #         print(f"{filePath} - Suspected or Infected")

    pageManager = GuiManager.ScreensManager()
    pageManager.RunCurrentPage()
    pageManager.ChangeCurrentPage(1)
    pageManager.RunCurrentPage()

if __name__ == "__main__":
    main()