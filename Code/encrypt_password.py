import hashlib
def encrypt_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
