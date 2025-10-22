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
