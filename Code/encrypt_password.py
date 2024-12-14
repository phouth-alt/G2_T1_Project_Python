#import hashlib library for hashing password
import hashlib
#function to hashing password
def encrypt_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
