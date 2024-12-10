from encrypt_password import encrypt_password
from check_information import check_password



def login(username, password):
    if check_password(username, password):
        return True
    else:
        return False

        
            