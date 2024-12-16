import os
from encrypt_password import encrypt_password

# Check password function for reset password that requires username and password
def check_password(username, password):
    try:
        # Dynamic file path generation for better portability
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "Database", "database.txt")
        
        # Encrypt the provided password
        en_password = encrypt_password(password)
        
        # Read the database file
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split("\t\t")
                if len(parts) > 2:  # Ensure line has at least username and password
                    if parts[0] == username and parts[2] == en_password:
                        return True
        return False
    
    except FileNotFoundError:
        print("Error: File not found. Please ensure the database exists.")
        return False
    except IOError:
        print("An error occurred while accessing the file.")
        return False

if __name__ == "__main__":
    # Test the function with a sample username and password
    result = check_password("vuth", "UareMYfarVoritH00@")
    print("Password Match:", result)
