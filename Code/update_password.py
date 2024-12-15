def update_password(new_password):
    try:
        file_path = "D:\G2_T1_Project_Python\Database\database.txt"
        with open(file_path,'a') as file:
            for line in file:
                 parts = line.strip().split("\t\t")
                 username = parts[0]
                 phone = parts[1]
                 if len(parts) == 3:
                      username, phone , new_password = parts
                      file.writelines(parts)
    except Exception as e:
        print("An error occurred:{}".format(e))