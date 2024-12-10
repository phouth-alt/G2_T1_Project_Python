from encrypt_password import encrypt_password
from check_information import check_user
from password_strength import pass_strength
#Function to reset password that require username and old password
def reset_pass(username,password):
    try:
        check_user(username,password)
        en_password = encrypt_password(password)
        if check_user(username,password):
            password = input("New password: ")
            pass_strength(password)
            if not pass_strength(password):
                return
            password = encrypt_password(password)
        else:
            print("Please try again")
            return
        file_path = "D:\G2_T1_Project\Data\data.txt"
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split("\t\t")
                if len(parts) > 2 and parts[0] == username:
                        parts[2][username] = password
    
                print("Password updated successfully!")
    except Exception as e:
        print("An error occurred:{}".format(e))

reset_pass("Phan Phouth","UareMYfarVoritH00@")