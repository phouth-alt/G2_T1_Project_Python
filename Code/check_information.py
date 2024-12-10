from encrypt_password import encrypt_password
#Create function for check if user already have account by using phone number
def check_username(phone):
     try:
          file_path = "D:\G2_T1_Project\Data\data.txt"
          #convert phone number from int to string
          phone = str(phone)
          #open file with mode read
          with open(file_path, 'r') as file:
               #store data as line when after read
               for line in file:
                    #slite line to 3 part
                    parts = line.strip().split("\t\t")
                    if len(parts) > 1:
                         #compair part2 that is phone number with phone number that user input
                         if parts[1].strip() == phone:
                              return True
          return False
     except FileNotFoundError:
        print("Error: File not found at {}".format(file_path))
#check user function use when user loginto account that already exist
def check_user(username,password):
     try:
          en_password = encrypt_password(password)
          file_path = "D:\G2_T1_Project\Data\data.txt"
          with open(file_path, 'r') as file:
               for line in file:
                    parts = line.strip().split("\t\t")
                    if len(parts) > 2:
                         #compair part1 that is username and part3 is password 
                         if parts[0].strip() == username and parts[2].strip() == en_password:
                              return True
          return False
     except FileNotFoundError:
        print("Error: File not found at {}".format(file_path))
#check password function use for reset password that need username and password
def check_password(username,password):
          try:
               file_path = "D:\G2_T1_Project\Data\data.txt"
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

