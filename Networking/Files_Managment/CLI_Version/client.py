import socket
import os

class Client:
    """A class which represents a client."""


    def __init__(self):
        print("███████╗██╗██╗     ███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗\n"
              "██╔════╝██║██║     ██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝\n"
              "█████╗  ██║██║     █████╗      ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║\n"
              "██╔══╝  ██║██║     ██╔══╝      ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║\n"
              "██║     ██║███████╗███████╗    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║\n"
              "╚═╝     ╚═╝╚══════╝╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝"
              "********************************************\n"
              "//         created by:Yuval Kuina         //\n"
              "********************************************\n")

        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect(("localhost", 1234))

        print("Connected to the server.")
        print("Client menu initialized.")


    def ChooseCommand(self):
        # The function makes the user to choose a command
        print("Menu:\n1. Upload File\n2. Download File\n3. Quit")
        while True:
            command = input("Enter your option: ")
            if command == "1":
                self.UploadFile()
            elif command == "2":
                self.DownloadFile()
            elif command == "3":
                self.Disconnect()
                break
            else:
                print("Invalid option. Please try again.")


    def UploadFile(self):
        # The function asks the user for a file and uploads it to the server
        filePath = input("Enter the file path: ")

        while not os.path.exists(filePath):
            print("The given path does not exist! Please try again.")
            filePath = input("Enter a valid file path: ")
        
        # send the name of the file
        self.clientSocket.send("1".encode())
        fileName = os.path.basename(filePath)
        self.clientSocket.send(fileName.encode())

        # send the size of the file
        self.clientSocket.send(str(os.stat(filePath).st_size).encode('utf8'))
        #print(os.stat(filePath).st_size)

        with open(filePath, "rb") as file:
            self.clientSocket.send(file.read())
        print(f"The file '{fileName}' successfully uploaded.")


    def DownloadFile(self):
        # The function presents the user the list of files from the database
        # and requests a file from the server and saves it locally.
        self.clientSocket.send("2".encode())

        filesNamesLength = int(str(self.clientSocket.recv(1024).decode("utf8")))
        filesNamesFromDatabase = (self.clientSocket.recv(filesNamesLength).decode()).split("*")[1:]
        maxLenOfName = 0
        for i in filesNamesFromDatabase:
            if len(i) > maxLenOfName:
                maxLenOfName = len(i)
        print(maxLenOfName-len(filesNamesFromDatabase[0]))
        print("======Database Files======")
        for i in range(len(filesNamesFromDatabase)):
            print("| -file- "+filesNamesFromDatabase[i]+" "*(maxLenOfName-len(filesNamesFromDatabase[i]))+' |')
        print("==========================")

        fileName = input("Enter the file name to download: ")
        self.clientSocket.send(fileName.encode())

        response = self.clientSocket.recv(1024).decode()
        fileSize = None
        if response == "File not found":
            print("The requested file does not exist on the server.")
        else:
            fileSize = int(str(self.clientSocket.recv(1024).decode("utf8")))
            with open(fileName, "wb") as file:
                file.write(self.clientSocket.recv(fileSize))
            print(f"File '{fileName}' successfully downloaded.")

    
    def Disconnect(self):
        # The function disconnects the client's socket.
        self.clientSocket.send("3".encode())
        self.clientSocket.close()
        print("Disconnected from the server.")


if __name__ == "__main__":
    client = Client()
    client.ChooseCommand()
