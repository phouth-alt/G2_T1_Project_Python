def update_password(username,phone,new_password):
    try:
        file_path = "D:\G2_T1_Project_Python\Database\database.txt"
        dict_update = {}
        with open(file_path,'r') as file:
            for line in file:
                 parts = line.strip().split("\t\t")
                 dict_update[parts[0]] = {parts[1].strip():parts[2].strip()}
                 if len(parts) == 3 and username == parts[0] and phone == parts[1]:
                      dict_update.update({parts[0] : {parts[1] : new_password}})
                      print(dict_update)
    except Exception as e:
        print("An error occurred:{}".format(e))



if __name__ == "__main__":
    update_password("phanphouth",85510686710,"UareMYfarVoritH00@")