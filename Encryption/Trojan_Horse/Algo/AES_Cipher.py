import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

class AESCipher:
    @staticmethod
    def aes_encrypt_decrypt(input_string: str, message: str, action: str) -> str:
        def create_aes_key_from_string(input_string: str) -> bytes:
            salt = os.urandom(16)  # Generate a random salt
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                             length=32,
                             salt=salt,
                             iterations=100000,
                             backend=default_backend())
            key = kdf.derive(input_string.encode())
            return key, salt

        def encrypt_message(key: bytes, message: str) -> bytes:
            iv = os.urandom(16)  # Generate a random initialization vector (IV)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            
            # Pad the message to be a multiple of 16 bytes using PKCS7 padding
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_message = padder.update(message.encode()) + padder.finalize()
            
            encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
            return iv + encrypted_message

        def decrypt_message(key: bytes, encrypted_message: bytes) -> str:
            iv = encrypted_message[:16]
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            
            decrypted_padded_message = decryptor.update(encrypted_message[16:]) + decryptor.finalize()
            
            # Remove PKCS7 padding
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            decrypted_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()
            
            return decrypted_message.decode().strip()

        key, salt = create_aes_key_from_string(input_string)
        # print(f"Derived AES Key: {key.hex()}")
        # print(f"Salt: {salt.hex()}")

        if action == 'encrypt':
            encrypted_message = encrypt_message(key, message)
            encrypted_message_with_salt = salt + encrypted_message
            encrypted_message_base64 = base64.b64encode(encrypted_message_with_salt).decode('utf-8')
            # print(f"Encrypted Message (base64): {encrypted_message_base64}")
            return encrypted_message_base64
        elif action == 'decrypt':
            encrypted_message_bytes = base64.b64decode(message.encode('utf-8'))
            salt = encrypted_message_bytes[:16]
            encrypted_message = encrypted_message_bytes[16:]
            key, _ = create_aes_key_from_string(input_string)  # Recreate the key with the same input string and salt
            decrypted_message = decrypt_message(key, encrypted_message)
            # print(f"Decrypted Message: {decrypted_message}")
            return decrypted_message
        else:
            raise ValueError("Invalid action. Use 'encrypt' or 'decrypt'.")
