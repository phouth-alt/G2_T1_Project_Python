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
            if check_user(username,password):
                return True  # Successfully logged in
            else:
                attempts += 1
                print("\tInvalid credentials. Attempt {} of {}.".format(attempts, max_attempts))

                if attempts < max_attempts:
                    username = input("\tEnter username again: ")
                    password = input("\tEnter password again: ")

        print("\tToo many failed attempts. Access denied.")
        return False  # Login failed

    except Exception as e:
        print("\tAn error occurred: {}".format(e))
        return False

if __name__ == "__main__":
    login("phouth","UareMYfarVoritH00@")