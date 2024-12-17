import os

def update_password(phone,new_password):
    try:
        file_path = "D:\G2_T1_Project_Python\Database\database.txt"
        temp_file_path = file_path + ".tmp"
        updated = False
        
        with open(file_path, 'r') as file, open(temp_file_path, 'w') as temp_file:
            for line in file:
                parts = line.strip().split("\t\t")
                if len(parts) == 3 and parts[1] == str(phone):
                    # Update the password for the matching phone number
                    updated_line = f"{parts[0]}\t\t{parts[1]}\t\t{new_password}\n"
                    temp_file.write(updated_line)
                    updated = True
                else:
                    # Write the original line
                    temp_file.write(line)
        
        # Replace the original file with the updated file
        if updated:
            os.replace(temp_file_path, file_path)
            print("\tPassword updated successfully for phone number: {}".format(phone))
        else:
            os.remove(temp_file_path)
            print("\tPhone number '{}' not found.".format(phone))
    
    except Exception as e:
        print("\tAn error occurred: {}".format(e))

if __name__ == "__main__":
    update_password(85510686710, "UareMYfarvoritH00")
