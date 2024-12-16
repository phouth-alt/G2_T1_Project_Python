import secrets
import string

def generate_alphanumeric_otp(length=6):
    """
    Generates a secure alphanumeric OTP of the given length.
    """
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    characters = string.ascii_letters + string.digits
    otp = ''.join(secrets.choice(characters) for _ in range(length))
    return otp

# Example usage
if __name__ == "__main__":
    print("Your secure alphanumeric OTP is:", generate_alphanumeric_otp())
