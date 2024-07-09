import mysql.connector
from SSL_Socket import SslSocket
import random

class Server:
    # A class which represents the server of the program.
    def __init__(self) -> None:
        # Creating an ssl socket
        self.serverSocket = SslSocket(isServer=True, sourceIp="0.0.0.0", sourcePort=1234, certFilePath="cert.crt", keyFilePath="private.key")

        self.mydb, self.mycursor = self.ConnectToDatabase()

        self.secretWord = self.GenerateASecretWord()

        # Save the secret word in the database table
        self.InsertDataIntoDatabase(content=self.secretWord)

        # Sending a random secret word to the client
        self.serverSocket.SendMsg(content=self.secretWord)

    def GenerateASecretWord(self):
        # The function gets nothing.
        # The function returns a new string which consists of 8 random letters.
        return ''.join([chr(random.randint(97, 122)) for i in range(8)])

    def ConnectToDatabase(self):
        # The function gets a database path as a parameter
        # The function connect to the given database or create a new one if no path was given.

        # Connect to the database
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="root",
                                       database="trojan_db")
        # Create a cursor object to execute queries
        mycursor = mydb.cursor()
        return mydb, mycursor

    def InsertDataIntoDatabase(self, content):
        # The function gets a string as a parameter.
        # The function adds the given string to the MySQL database of the server.

        # Create the database if it doesn't exist.
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS table1 (secretword VARCHAR(8))")
        # Add the given content to the secretword column in the table
        self.mycursor.execute(f"INSERT INTO table1 (secretword) VALUES ('{content[0:8]}')")
        self.mydb.commit()
        print("The secret word was added to the database successfully!")

if __name__ == "__main__":
    serverObject = Server()
