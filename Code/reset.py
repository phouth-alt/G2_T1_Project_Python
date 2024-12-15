#import modual
from encrypt_password import encrypt_password
from reset_check import check_user
from save_to_file import update_password
from password_strength import pass_strength
#Function to reset password that require username and old password
def reset_pass(username,password,new_password):
    try:
        #check if provide information equal to information storage
        if check_user(username,password):
            #check new password strength if not it will return 
            if not pass_strength(new_password):
                return
            #hashing new password
            new_password = encrypt_password(new_password)
            update_password(new_password)
        else:
            print("Please try again")
            return
    except Exception as e:
        print("An error occurred:{}".format(e))




if __name__ == "__main__":
    reset_pass("phanphouth","usenn0398U@")