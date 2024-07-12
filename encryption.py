from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(input_file, output_file, key):
    f = Fernet(key)
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    f = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
