from encrypt_password import encrypt_password
from login_check import check_password

attempt = 0
max_attempt = 3
def create_user(username, password):
    file_path = "data.txt"
    try:
        en_password = encrypt_password(password)
        with open(file_path, "a") as file:  # 'a' mode appends to the file
            file.write(f"{username}\t{en_password}\n")
        print("User created successfully.")
    except IOError:
        print("An error occurred while writing to the file.")

def login(username, password):
    while attempt < max_attempt:    
        if check_password(username, password):
            return True
        else:
            attempt += 1
            remaining = max_attempt - attempt
            print("Invalid username or password. Please try again within remaining {remaining} attempt left.")
            return False