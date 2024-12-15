from encrypt_password import encrypt_password
from login_check import check_user

def login(username, password):
    """
    Attempts to log in a user by checking their username and password.
    """
    try:
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            if check_user(username, encrypt_password(password)):
                print("Login successful!")
                return True  # Successfully logged in
            else:
                attempts += 1
                print("Invalid credentials. Attempt {} of {}.".format(attempts, max_attempts))

                if attempts < max_attempts:
                    username = input("Enter username again: ")
                    password = input("Enter password again: ")

        print("Too many failed attempts. Access denied.")
        return False  # Login failed

    except Exception as e:
        print("An error occurred: {}".format(e))
        return False

if __name__ == "__main__":
    login("vuth","UareMYfarVoritH00@")