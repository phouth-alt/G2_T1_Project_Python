def recover_password(username, key_pin, new_password):  
    """Recover a user's password using the key pin."""  
    users = []  
    user_found = False
    try:  
        with open('users.txt', 'r') as file:  
            users = file.readlines()  
        
        with open('users.txt', 'w') as file:  
            for user in users:  
                stored_username, stored_password, stored_key_pin = user.strip().split(',')  
                if stored_username == username and stored_key_pin == key_pin:  
                    file.write(f"{stored_username},{new_password},{stored_key_pin}\n")  
                    print("Password recovered successfully. You can now log in with your new password.")  
                    user_found = True  
                else:  
                    file.write(user)  
        
        if not user_found:  
            print("Invalid username or key pin. Password recovery failed.")  

    except FileNotFoundError:  
        print("No users registered yet.")  