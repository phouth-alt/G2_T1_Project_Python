#import re modual for regular express matching 
import re
#function to check Password strength
def pass_strength(password):
        #check length of password if it less than or equal to 8 return False
        if(len(password) <= 8):
            print("Password Must be longer than 8 characters.")
            return False
        #check if password has no lower case character return value False
        elif not re.search("[a-z]",password):
            print("Password Must contain at least one lowercase letter.")
            return False
        #check if password has no upper case character return False
        elif not re.search("[A-Z]",password):
            print("Password Must contain at least one uppercase letter.")
            return False
        #check if password has no digit it will return False
        elif not re.search("[0-9]",password):
            print("Password Must contain at least on digit.")
            return False
        #check if password has no spacial character return False
        elif not re.search("[!@#$%^&*()]",password):
            print("Password Must contain at least one special character(!@#$%^&*()).")
            return False
               #check if password has white space return False
        elif re.search("\s",password):
            print("Password Must not contain whitespace.")
            return False
        #return True if no one condition is True
        else:
            return True

        
#test
if __name__ == "__main__":
     pass_strength("iloveyoubaby")
     pass_strength("Iloveubaby")
     pass_strength("1lovEubaby")
     print(pass_strength("1loveUb@by"))