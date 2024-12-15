from encrypt_password import encrypt_password
#check password function use for reset password that need username and password
def check_password(username,password):
          try:
               file_path = "D:\G2_T1_Project_Python\Database\database.txt"
               en_password = encrypt_password(password)
               with open(file_path, "r") as file:
                    for line in file:
                         parts = line.strip().split("\t\t")
                         if len(parts) > 1:
                              if parts[0] == username and parts[2] == en_password:
                                   return True
               return False
          except FileNotFoundError:
               print("Error file is not found.")
               return False
          except IOError:
               print("An error occurred while reading the file.")
               return False

if __name__ == "__main__":
     print(check_password("vuth","UareMYfarVoritH00@"))