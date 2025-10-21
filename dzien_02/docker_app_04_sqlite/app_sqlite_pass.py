import sqlite3
import os
import hashlib
import binascii

def hash_password(password):
    # Generate a random salt
    salt = os.urandom(16)
    # Use PBKDF2-HMAC-SHA256 with 100,000 iterations
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    # Convert the hash and salt to hexadecimal strings for storage
    return binascii.hexlify(salt).decode(), binascii.hexlify(hashed).decode()

def verify_password(stored_salt: str, stored_hash: str, input_password: str) -> bool:
    salt = binascii.unhexlify(stored_salt)
    hashed = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 100000)
    return binascii.hexlify(hashed).decode() == stored_hash

# Example usage
password = "my_secret_password"
salt, hashed_password = hash_password(password)

print("Salt:", salt)
print("Hashed password:", hashed_password)

# Verification
print("Password valid?", verify_password(salt, hashed_password, "my_secret_password"))
print("Password valid?", verify_password(salt, hashed_password, "wrong_password"))
# plik bazy



database = "users.db"
table_name = "users_data"
field_1 = "username"
field_2 = "password"


if os.path.exists(database):
    connection = sqlite3.connect(database)
else:
    print("Brak pliku!!!!")
    exit(0)

print("OK - działamy dalej")
cursor = connection.cursor()

while True:
    print("END - koniec wprowadzania.")
    login = input("Podaj login: ")
    if login == "END":
        connection.close()
        exit(0)
        
    passw = input("Podaj hasło: ")
    salt, hashed_password = hash_password(passw)
        
    values = (login, hashed_password, salt)
    try:
        cursor.execute(f'INSERT INTO {table_name} ("username","password","salt") VALUES (?,?,?)', values)
        connection.commit()
        print(f"Login {login} dodany poprawnie")
    except Exception as e:
        print(f"Wystąpił błąd dodania - {e}.")
        
