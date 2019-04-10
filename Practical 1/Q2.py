import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(data):
    kdf1 = PBKDF2HMAC(
        algorithm=hashes.SHA1(),
        length=32,
        salt=b'569',
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf1.derive(b'reza'))
    fer = Fernet(key)
    encrypted = fer.encrypt(bytes(data, "utf-8")).decode("utf-8")
    return encrypted

def decrypt(data):
    kdf1 = PBKDF2HMAC(
        algorithm=hashes.SHA1(),
        length=32,
        salt=b'569',
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf1.derive(b'reza'))
    fer = Fernet(key)
    decrypted = fer.decrypt(bytes(data, "utf-8")).decode("utf-8")
    return decrypted

plain = "9431035"
cipher = encrypt(plain)
decypher = decrypt(cipher)
print(plain, " -> ", cipher, " -> ", decypher)