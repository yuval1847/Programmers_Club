import os
import socket

class Server:
    """A class which represent a server."""
    
    
    def __init__(self, directoryPath):
        print("███████╗██╗██╗     ███████╗    ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗\n" 
              "██╔════╝██║██║     ██╔════╝    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗\n"
              "█████╗  ██║██║     █████╗      ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝\n"
              "██╔══╝  ██║██║     ██╔══╝      ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗\n"
              "██║     ██║███████╗███████╗    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║\n"
              "╚═╝     ╚═╝╚══════╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝\n"
              "********************************************\n"
              "//         created by:Yuval Kuina         //\n"
              "********************************************\n")
        
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind(("0.0.0.0", 1234))
        self.serverSocket.listen(1)
        self.directoryDatabasePath = directoryPath

        if not os.path.exists(self.directoryDatabasePath):
            os.makedirs(self.directoryDatabasePath)
            print(f"Files Directory '{self.directoryDatabasePath}' created.")
        else:
            print(f"Files Directory '{self.directoryDatabasePath}' already exists.")
        
        print("Server is listening on port 1234...")
        self.clientSocket, self.clientAddress = self.serverSocket.accept()
        print(f"Client connected from {self.clientAddress}")

    def GetCommands(self):
        # The function gets commands from the client.
        while True:
            data = self.clientSocket.recv(1024).decode()
            if data == "1":
                self.GetFileFromClient()
            elif data == "2":
                self.SendFile()
            elif data == "3":
                self.Disconnect()
                break
            else:
                print("Invalid command received from client")


    def GetFileFromClient(self):
        # The function receives the file from the client and saves it to the server's directory

        fileName = self.clientSocket.recv(1024).decode() 
        fileSize = int(str(self.clientSocket.recv(1024).decode("utf8")))        
        filePath = os.path.join(self.directoryDatabasePath, fileName)
        with open(filePath, "wb") as file:
            file.write(self.clientSocket.recv(fileSize))
        print(f"The file '{fileName}' successfully uploaded!")


    def SendFile(self):
        # The function sends a list of file names and the requested file to the client if it exists
        
        os.chdir(self.directoryDatabasePath)
        listOfFilesInDatabase = os.listdir()
        filesNames = ""
        for i in listOfFilesInDatabase:
            filesNames+="*"+i
        self.clientSocket.send(str(len(filesNames)*4).encode('utf8'))
        self.clientSocket.send(filesNames.encode())

        fileName = self.clientSocket.recv(1024).decode()
        filePath = os.path.join(self.directoryDatabasePath, fileName)
        
        if os.path.exists(filePath):
            self.clientSocket.send(fileName.encode())
            self.clientSocket.send(str(os.stat(filePath).st_size).encode('utf8'))
            with open(filePath, "rb") as file:
                self.clientSocket.send(file.read())
            print(f"The file '{fileName}' successfully sent!")
        else:
            self.clientSocket.send("File not found".encode())


    def Disconnect(self):
        # The function closes the server and client sockets
        self.clientSocket.close()
        self.serverSocket.close()
        print("Disconnected!")


if __name__ == "__main__":
    server = Server(directoryPath=os.path.join(os.getcwd(), "FilesDirectory"))
    server.GetCommands()
