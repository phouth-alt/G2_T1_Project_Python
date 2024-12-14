from encrypt_password import encrypt_password
from check_information import check_user
from save_to_file import update_password
from password_strength import pass_strength
#Function to reset password that require username and old password
def reset_pass(username,password,new_password):
    try:
        if check_user(username,password):
            if not pass_strength(new_password):
                return
            new_password = encrypt_password(new_password)
        else:
            print("Please try again")
            return
    except Exception as e:
        print("An error occurred:{}".format(e))
if __name__ == "__main__":
    reset_pass("phanphouth","usenn0398U@")