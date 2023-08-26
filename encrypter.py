from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(password.encode('utf-8'))
    return encrypted_data

def decrypt_password(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data

def main():
    key = generate_key()
    password = "supersecretpassword"

    encrypted_password = encrypt_password(password, key)
    print("Encrypted Password:", encrypted_password)

    decrypted_password = decrypt_password(encrypted_password, key)
    print("Decrypted Password:", decrypted_password)

if __name__ == "__main__":
    main()
