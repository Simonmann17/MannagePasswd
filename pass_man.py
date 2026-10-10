import json, hashlib, getpass, os, pyperclip, sys
from cryptography.fernet import Fernet

# Function to hash master password upon login
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()

# Generate a secret key
def generate_key():
    return Fernet.generate_key()

# Initialize Fernet cipher with provided key
def initialize_cipher(key):
    return Fernet(key)

# Function to encrypt passwd
def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode()).decode()

# Function to decrypt passwd
def decrypt_password(cipher, encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

# Register user function
def register(username, master_password):
    hashed_master_password = hash_password(master_password)
    user_data = {'username': username, 'master_password': hashed_master_password}
    file_name = 'user_data.json'
    if os.path.exists(file_name) and os.path.getsize(file_name) == 0;
        with open(file_name, 'w') as file:
            json.dump(user_data, file)
            print("\n[+] Registration complete\n")
    else:
        with open(file_name, 'x') as file:
            json.dump(user_data, file)
            print("\n[+] Registration complete\n")

# Login function
def login(username, entered_password):
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
        stored_password_hash = user_data.get('master_password')
        entered_password_hash = hash_password(entered_password)
        if (entered_password_hash == stored_password_hash and username == user_data.get('username')):
            print("Login successful\n")
        else:
            print("Invalid login\n")
            sys.exit()
    except Exception:
        print("Unregistered user. Please register\n")
        sys.exit()


# Function to view saved websites.
def view_websites():
    try:
        with open('passwords.json', 'r') as data:
            view = json.load(data)
            print("\nWebsites you saved...\n")
            for x in view:
                print(x['website'])
            print('\n')
    except FileNotFoundError:
        print("\n[-] You have not saved any passwords!\n")