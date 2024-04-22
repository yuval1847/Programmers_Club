import requests
import hashlib


LEVEL_OF_STRENGTH = [
    "is weak",
    "is vulnerable",
    "is strong",
    "is very strong",
    "is impenetrable"
]
ALFA_BYTE_UPPERCASE = [chr(i) for i in range(ord('A'), ord('Z')+1)]
ALFA_BYTE_LOWERCASE = [chr(i) for i in range(ord('a'), ord('z')+1)]
DIGITS = [str(i) for i in range(0, 10)]
SPECIAL_SIGNS = [chr(i) for i in range(ord('!'), ord(')')+1)]


def IsCommonPassword(password):
    # The function get a string which represent a password.
    # The function return True if the password is common, otherwise the function return False.

    # Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    # Take only the first 5 characters of the hash to search the API
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    # Make a request to the HIBP API
    response = requests.get(url)
    if response.status_code == 200:
        # Check if the suffix of the hash exists in the response
        return suffix in response.text
    else:
        # If the request fails, print that there is an error
        print("Error checking password against HIBP API")
        return False
    
def IsIn(list_of_chars, password):
    # The function get a list of chars that should be check in the given sting.
    # The fucntion return true if there is at least one char that both inside the list an in the string.
    for i in list_of_chars:
         if i in password:
              return True
    return False 

def CheckingPassword(password):
    # The function get a password to check as a string.
    # The function return a string which represent the level of strength of the password.
    
    index_level_of_strength = 0

    # Checking if there is a common password or pharse in the password itself
    if IsCommonPassword(password):
        return "The password is too weak because it's popular so it's banned.\nYou need to replace it with another password immediately!"
    
    # Checking the length of the password
    if len(password) < 8:
        return "The password is too weak because it's shorter than 8 digits"
    
    if len(password) >= 16:
        index_level_of_strength += 1


    # Checking for lowercase, uppercase, numbers and special signs
    if IsIn(ALFA_BYTE_LOWERCASE, password) or IsIn(ALFA_BYTE_UPPERCASE, password):
        index_level_of_strength += 1
        if IsIn(ALFA_BYTE_LOWERCASE, password) and IsIn(ALFA_BYTE_UPPERCASE, password):
            index_level_of_strength += 1

    if IsIn(DIGITS, password):
        index_level_of_strength += 1

    if IsIn(SPECIAL_SIGNS, password):
            index_level_of_strength += 1

    return f"The entered password {LEVEL_OF_STRENGTH[index_level_of_strength]}!"    

def main():
    print("Welcome to my password security checking evaluator!")
    print(CheckingPassword(input("Enter a password for checking: ")))

if __name__ == "__main__":
     main()