from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def aes_encrypt_decrypt(input_string: str, message: str, action: str) -> bytes:
    def create_aes_key_from_string(input_string: str) -> bytes:
        salt = os.urandom(16)  # Generate a random salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(input_string.encode())
        return key, salt

    def encrypt_message(key: bytes, message: str) -> bytes:
        iv = os.urandom(16)  # Generate a random initialization vector (IV)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_message = message + (16 - len(message) % 16) * ' '  # Pad the message to be a multiple of 16 bytes
        encrypted_message = encryptor.update(padded_message.encode()) + encryptor.finalize()
        return iv + encrypted_message

    def decrypt_message(key: bytes, encrypted_message: bytes) -> str:
        iv = encrypted_message[:16]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_message = decryptor.update(encrypted_message[16:]) + decryptor.finalize()
        return decrypted_message.decode().strip()

    key, salt = create_aes_key_from_string(input_string)
    print(f"Derived AES Key: {key.hex()}")
    print(f"Salt: {salt.hex()}")

    if action == 'encrypt':
        encrypted_message = encrypt_message(key, message)
        print(f"Encrypted Message: {encrypted_message.hex()}")
        return encrypted_message
    elif action == 'decrypt':
        decrypted_message = decrypt_message(key, bytes.fromhex(message))
        print(f"Decrypted Message: {decrypted_message}")
        return decrypted_message
    else:
        raise ValueError("Invalid action. Use 'encrypt' or 'decrypt'.")