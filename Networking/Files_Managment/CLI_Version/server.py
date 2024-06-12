import os
import socket

class Server:
    """A class which represent a server."""

    def __init__(self, directoryPath):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind(("0.0.0.0", 1234))
        self.serverSocket.listen()
        self.directoryDatabasePath = directoryPath
        self.currentFileName = None
        self.clientSocket, self.clientAddress = self.server_socket.accept()

        print("███████╗██╗██╗     ███████╗    ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗\n" 
              "██╔════╝██║██║     ██╔════╝    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗\n"
              "█████╗  ██║██║     █████╗      ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝\n"
              "██╔══╝  ██║██║     ██╔══╝      ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗\n"
              "██║     ██║███████╗███████╗    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║\n"
              "╚═╝     ╚═╝╚══════╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝\n")
        print("********************************************\n"
              "//         created by:Yuval Kuina         //\n"
              "********************************************\n")
        
        print("CLIENT CONNECTED!")

        
    def GetCommands(self):
        # The function gets commands from the client.
        # The function returns 
        data = None
        while True:
            data = server.clientSocket.recv(1024).decode()
            if data == "1":
                server.GetFileFromClient()
            elif data == "2":
                server.SendFile()
            elif data == "3":
                print("Disconnecting now...")
                server.Disconnect()
                break
        

    def GetListOfFiles(self):
        # The function gets nothing.
        # The function returns a list of string which contain the names of all the files in the database directory.
        try:
            if os.path.exists(self.directoryDatabasePath):
                filesList = os.listdir(self.directoryDatabasePath)
            
        except Exception as e:
            print(f"An error occurred: {e}")
        return []


    def GetFileFromClient(self):
        # The function gets nothing.
        # The function insert the client's file to the server's database(directory of files)
        # and send '1' if the files where uploaded successfully, otherwise '2'
        try:
            fileName = self.serverSocket.recv(4096).decode() 
            fileContent = self.serverSocket.recv(4096).decode()
            with open(self.directoryDatabasePath + "\\" + fileName, "w") as Newfile:
                Newfile.write(fileContent)
            self.clientSocket.send("1".encode())
        except Exception:
            self.clientSocket.send("2".encode())


    def SendFile(self):
        # The function gets nothing.
        # The function send the file, if it exists, from the database, otherwise None.
        fileName = self.clientSocket.recv(4096).decode()
        listOfFiles = self.GetListOfFiles()
        fileContent = None
        if fileName in listOfFiles:
            fileContent = self.directoryDatabasePath + "\\" + fileName
        self.clientSocket.send(fileContent.encode())
        
    
    def Disconnect(self):
        # The function gets nothing.
        # The function close the sockets of the client and the server.
        self.serverSocket.close()
        self.clientSocket.close()


if __name__ == "__main__":
    # Define the folder path
    folderPath = os.path.join(os.getcwd(), "My_Folder")

    # Check if the folder exists
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
        print(f"Files Directory '{folderPath}' created.")
    else:
        print(f"Files Directory '{folderPath}' already exists.")

    server = Server(directoryPath=os.path.join(os.getcwd(), "FilesDirectory"))
    server.GetCommands()
    


# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(("0.0.0.0", 1234))
# server_socket.listen()
# print("SERVER UP\nSERVER RUNNING")
# (client_socket, client_address) = server_socket.accept()
# print("CLIENT CONNECTED!")

# # while True:
# #     data = client_socket.recv(1024).decode()
# #     print(f"Client: {data}")
# #     # A known agreement to finish the connection with the client(if the client send the string "Quit,
# #     # so close the connection with him by sending him the string "client shut down"
# #     if data == "Quit":
# #         print("Closing client socket now...")
# #         client_socket.send("client shut down".encode())
# #         break
# #     elif data in server_commands_dictionary:
# #         data = server_commands_dictionary[data]

# #     client_socket.send(str(data).encode())

