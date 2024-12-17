#import modual from another file
from register_check import check_username
from password_strength import pass_strength
from save_to_file import save_to_file
#Create register function that required username, password, phone number
def register(username,password,phone):
    #username, password,phone number should fields if not it will return
    if not username or not password or not phone:       
        print("\tError : All fields (username, password, phone) are required.")
        return
    #check if user already has account or new user by phone number
    if check_username(phone):
        print("\tyour alread have an account. please login")
        return
    #check Password Strength when user register
    if not pass_strength(password):
        return
    #save username, password, phone number to database
    save_to_file(username,password,phone)

if __name__ == "__main__":
    register("phanphouth","kshjdUlje0399@",+855976899776)