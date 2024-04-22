# The key value of the XOR gate
XOR_KEY = 5

def EncryptFile(filePath):
    # The function get a file path.
    # The function enrypt the file according to XOR 5 gate.
    with open(filePath, 'r+b') as f:
        currentByte = f.read(1)
        while currentByte:
            encryptedByte = [currentByte[0] ^ XOR_KEY]
            f.seek(-1, 1)
            f.write(bytes(encryptedByte))
            currentByte = f.read(1)

def main():
    print("Welcome to my file XOR encryption software!\nMy software is using XOR gate with a value of 5(in decimal) for the encryption\n")
    print("Options:\n* 1.Encrypting\n* 2.Decrypting")
    
    menuUserChoice = int(input("Wanted operation: "))
    while not 1 <= menuUserChoice <= 2:
        print("The option should be 1 or 2, try again")
        menuUserChoice = int(input("Wanted operation: "))

    filePath = input("Enter a file path: ")
    # The repeating of the XOR encryption on the encrypted file with the same key actually decrypt the file.
    EncryptFile(filePath)
    
    if menuUserChoice == 1:
        print("The file got successfuly encrypted!")
    else:
        print("The file got successfuly decrypted!")


if __name__ == "__main__":
    main()