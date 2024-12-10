from encrypt_pass import encrypt_password
from check_username import check_password



def login(username, password):
    if check_password(username, password):
        return True
    else:
        return False

        
            