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

        self.clientSocket.send("1".encode())
        fileName = os.path.basename(filePath)
        self.clientSocket.send(fileName.encode())

        with open(filePath, "r") as file:
            self.clientSocket.send(file.read().encode())
        print(f"The file '{fileName}' successfully uploaded.")


    def DownloadFile(self):
        # The function requests a file from the server and saves it locally
        self.clientSocket.send("2".encode())
        fileName = input("Enter the file name to download: ")
        self.clientSocket.send(fileName.encode())

        response = self.clientSocket.recv(1024).decode()
        if response == "File not found":
            print("The requested file does not exist on the server.")
        else:
            with open(fileName, "w") as file:
                file.write(self.clientSocket.recv(4096).decode())
            print(f"File '{fileName}' successfully downloaded.")

    
    def Disconnect(self):
        # The function gets nothing.
        # The function disconnect the client's socket.
        self.clientSocket.send("3".encode())
        self.clientSocket.close()
        print("Disconnected from the server.")

if __name__ == "__main__":
    client = Client()
    client.ChooseCommand()
