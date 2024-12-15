from encrypt_password import encrypt_password
#check user function use when user loginto account that already exist
def check_user(username,password):
     try:
          #hashing password
          en_password = encrypt_password(password)
          #open database file
          file_path = "D:\G2_T1_Project_Python\Database\database.txt"
          with open(file_path, 'r') as file:
               for line in file:
                    parts = line.strip().split("\t\t")
                    #check length of parts                 
                    if len(parts) > 2:
                         #compair part1 that is username and part3 is password 
                         username_in_database = parts[0]
                         password_in_database = parts[2]
                         if username_in_database == username and password_in_database == en_password:
                              return True
          return False
     except FileNotFoundError:
        print("Error: File not found at {}".format(file_path))