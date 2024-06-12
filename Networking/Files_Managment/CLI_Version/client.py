import socket
import os

class Client:
    """A class which represent a client"""

    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((socket.gethostname(), 1234))


        print("███████╗██╗██╗     ███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗\n"
              "██╔════╝██║██║     ██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝\n"
              "█████╗  ██║██║     █████╗      ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║\n"
              "██╔══╝  ██║██║     ██╔══╝      ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║\n"
              "██║     ██║███████╗███████╗    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║\n"
              "╚═╝     ╚═╝╚══════╝╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝"
              "********************************************\n"
              "//         created by:Yuval Kuina         //\n"
              "********************************************\n")


    def ChooseCommand(self):
        # The function gets nothing.
        # The function makes the user's choose a command.
        print("Menu:\n1. Upload File\n2. Download File\n3. Quit")
        while True:
            message_to_the_server = input("Enter your option: ")
            if message_to_the_server == "1" or message_to_the_server.lower() == "upload file":
                
                self.UploadFile()
            elif message_to_the_server == "2" or message_to_the_server.lower() == "download file":
                self.clientSocket.send("2".encode())
                self.DownloadFile()
            elif message_to_the_server == "3" or message_to_the_server.lower() == "quit":
                self.clientSocket.send("3".encode())
                self.clientSocket.close()
                quit()
            else:
                print("The given command doesn't exist!")


    def UploadFile(self):
        # The function asks the user for a file.
        # The function send the server the choosen file.
        filePath = input("Enter a file path:")

        while not os.path.exists(filePath):
            print("The given path doesn't exist!, please try again")
            filePath = input("Enter a file path(the full path):")
        
        self.clientSocket.send("1".encode())
        
        # Send the file name.
        self.clientSocket.send(filePath.split("\\")[-1])

        # Send the file content.
        with open(filePath, "r") as file:
            self.clientSocket.send(file.read().encode())
                

    def DownloadFile(self):
        # The function gets nothing.
        # The function gets the content of the file and create it on the choosen path.
        fileName = self.clientSocket.recv(4096).decode()
        newFileContent = self.clientSocket.recv(4096).decode()

        with open(fileName, "w") as Newfile:
            Newfile.write(newFileContent)


    def Disconnect(self):
        # The function gets nothing.
        # The function close the socket of the current client.
        self.clientSocket.close()
        print("CLIENT SHUTDOWN")


if __name__ == "__main__":
    client = Client()
    client.ChooseCommand()
