#import encrypt password modual
from encrypt_password import encrypt_password
#Create Save to file function for save username, password, phone number to datadbase
def save_to_file(username,password,phone):
        try:
            #Encrypt password for secure before save to database
            password = encrypt_password(password)
            #Nested dictionary for store data in short period(Ex:{username:{phone:password}})
            data_dict = {}
            data_dict[username] = {phone : password}
            file_path = "D:\G2_T1_Project_Python\Database\database.txt"
            #Open file to append data
            with open(file_path, "a") as file:
                for username, details in data_dict.items():
                    for phone, password in details.items():
                        file.write('%s\t\t%s\t\t%s\n' %(username,phone, password))
            print("\tyour registration completed.")    
        except IOError as e: 
             print("\tFile error: {}".format(e))



#test function block     
if __name__ == "__main__":
    save_to_file("phanphouth","usenn0398U@",855976899776)  
       