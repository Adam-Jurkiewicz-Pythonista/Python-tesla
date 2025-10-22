import os
import hashlib
import binascii

def hash_password(password, salt_bits=32, iterations=100000):
    """
    PBKDF2-HMAC-SHA256 hash function
    :param password:
    :param salt_bits: bits for urandom, default 32
    :param iterations: number of iterations, default 100000
    :return: tuple (salt, hashed pass with hex)
    """
    # Generate a random salt
    salt = os.urandom(salt_bits)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations=iterations)
    return salt, hashed
    # Convert the hash and salt to hexadecimal strings for storage
    return binascii.hexlify(salt).decode(), binascii.hexlify(hashed).decode()

def verify_password(stored_salt: str, stored_hash: str, input_password: str) -> bool:
    salt = binascii.unhexlify(stored_salt)
    hashed = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 100000)
    return binascii.hexlify(hashed).decode() == stored_hash
