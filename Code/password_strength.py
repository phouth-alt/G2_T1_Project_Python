#import re modual for regular express matching 
import re
#function to check Password strength
def password_strength(password):
        #check length of password if it less than or equal to 8 return False
        if(len(password) <= 8):
            print("\tPassword Must be longer than 8 characters.")
            #check if password has no lower case character return value False
            if not re.search("[a-z]",password):
                print("\tPassword Must contain at least one lowercase letter.")
            #check if password has no upper case character return False
            if not re.search("[A-Z]",password):
                print("\tPassword Must contain at least one uppercase letter.")
            #check if password has no digit it will return False
            if not re.search("[0-9]",password):
                print("\tPassword Must contain at least on digit.")
            #check if password has no spacial character return False
            if not re.search("[!@#$%^&*()]",password):
                print("\tPassword Must contain at least one special character(!@#$%^&*()).")
                #check if password has white space return False
            if re.search("\s",password):
                print("\tPassword Must not contain whitespace.")
            #return True if no one condition is True
        else:
            print("\tStrong password")
            return True

        
#test
if __name__ == "__main__":
    password_strength("oejoe")  