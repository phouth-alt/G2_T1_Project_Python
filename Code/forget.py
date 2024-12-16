from generateOTP import generate_alphanumeric_otp
def recover_password(phone):  
    """Recover a user's password using the key pin."""  
    file_path = "D:\G2_T1_Project_Python\Database\database.txt"
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split("\t\t")
            if parts[1] == phone:
                return True
    return False
