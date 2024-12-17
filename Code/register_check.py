from encrypt_password import encrypt_password
#Create function for check if user already have account by using phone number
def check_username(phone):
     try:
          file_path = "D:\G2_T1_Project_Python\Database\database.txt"
          #convert phone number from integer to string
          phone = str(phone)
          #open file with mode read
          with open(file_path, 'r') as file:
               #store data as line when after read
               for line in file:
                    #slite line to 3 part
                    parts = line.strip().split("\t\t")
                    if len(parts) > 1:
                         #compair part2 that is phone number in database with phone number that user input
                         phone_in_database = parts[1].strip() 
                         if phone_in_database == phone:
                              #if it equal return value True
                              return True
          #if not equal return value False
          return False
     #if file not found it will show a message
     except FileNotFoundError:
        print("\tError: File not found at {}".format(file_path))

if __name__ == "__main__":
     print(check_username(855976899776))
     