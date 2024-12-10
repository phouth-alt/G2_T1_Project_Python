#import modual from another file
from check_username import check_username
from pass_strength import pass_strength
from save_to_file import save_to_file
#Create register function that required username, password, phone number
def register(username,password,phone):
    #username, password,phone number should fields if not it will return
    if not username or not password or not phone:
        print("Error : All fields (username, password, phone) are required.")
        return
    #check if user already has account or new user by phone number
    if check_username(phone) == True:
        print("your alread have an account. please login")
        return
    #check Password Strength when user register
    if not pass_strength(password):
        return
    #save username, password, phone number to database
    save_to_file(username,password,phone)
