from register import register
from reset import reset_pass
from login import login
from forget import recover_password
from generateOTP import generate_alphanumeric_otp
from update_password import update_password
from encrypt_password import encrypt_password
from password_strength import pass_strength

# Base class for handling user authentication and related tasks
class UserAuthentication:
    def __init__(self, username=None, password=None, phone=None):
        self.username = username
        self.password = password
        self.phone = phone

    def set_user_info(self, username, password, phone=None):
        self.username = username
        self.password = password
        self.phone = phone

    def validate_password_strength(self, password):
        return pass_strength(password)

    def encrypt_user_password(self, password):
        return encrypt_password(password)


# Login class that inherits from UserAuthentication
class Login(UserAuthentication):
    def __init__(self, username, password):
        super().__init__(username, password)

    def authenticate(self):
        # Authentication logic using the parent class methods
        if login(self.username, self.password):
            return "Login successful"
        else:
            return "Invalid username or password"


# Register class that inherits from UserAuthentication
class Register(UserAuthentication):
    def __init__(self, username, password, phone):
        super().__init__(username, password, phone)

    def register_user(self):
        # Registration logic using the parent class methods
        encrypted_password = self.encrypt_user_password(self.password)
        register(self.username, encrypted_password, self.phone)
        return f"User {self.username} registered successfully"


# Password Reset class that inherits from UserAuthentication
class PasswordReset(UserAuthentication):
    def __init__(self, username, password, phone):
        super().__init__(username, password, phone)

    def reset_user_password(self, new_password):
        # Password reset logic
        encrypted_new_password = self.encrypt_user_password(new_password)
        reset_pass(self.username, self.password, self.phone, encrypted_new_password)
        return "Password reset successful"


# Password Recovery class that inherits from UserAuthentication
class PasswordRecovery(UserAuthentication):
    def __init__(self, phone):
        super().__init__(phone=phone)

    def recover_account(self):
        # Account recovery logic
        if recover_password(self.phone):
            otp = generate_alphanumeric_otp()  # Generate OTP
            return otp
        else:
            return "Account recovery failed"


# Main class for managing options and interactions
class AuthenticationSystem:
    def __init__(self):
        self.user = None

    def display_menu(self):
        print("--------------------------------------------")
        print("-----------Authentication System------------")
        print("--------------------------------------------")
        print("1.Login")
        print("2.Register")
        print("3.Reset Password")
        print("4.Forget Password")
        print("5.Exit program")
        print("--------------------------------------------")
        print("-------------Enter an option----------------")
        print("--------------------------------------------")

    def get_user_input(self, prompt):
        return input(prompt).strip()

    def execute(self):
        while True:
            self.display_menu()
            option = self.get_user_input("")
            
            if option == '1':  # Login
                username = self.get_user_input("Username: ")
                password = self.get_user_input("Enter password: ")
                login_obj = Login(username, password)
                print(login_obj.authenticate())
            
            elif option == '2':  # Register
                username = self.get_user_input("Username: ")
                password = self.get_user_input("Enter password: ")
                phone = self.get_user_input("Phone number: ")
                register_obj = Register(username, password, phone)
                print(register_obj.register_user())
            
            elif option == '3':  # Reset Password
                username = self.get_user_input("Enter username: ")
                phone = self.get_user_input("Phone number: ")
                password = self.get_user_input("Enter current password: ")
                new_password = self.get_user_input("Enter new password: ")
                reset_obj = PasswordReset(username, password, phone)
                print(reset_obj.reset_user_password(new_password))
            
            elif option == '4':  # Forget Password
                phone = self.get_user_input("Phone number: ")
                recovery_obj = PasswordRecovery(phone)
                otp = recovery_obj.recover_account()
                print(f"Your OTP is: {otp}")
                input_otp = self.get_user_input("Enter your OTP: ")
                if input_otp == otp:
                    new_password = self.get_user_input("New password: ")
                    if pass_strength(new_password):
                        encrypted_new_password = encrypt_password(new_password)
                        update_password(phone, encrypted_new_password)
                        print("Password updated successfully")
                    else:
                        print("Password does not meet strength requirements")
                else:
                    print("Invalid OTP")

            elif option == '5':  # Exit Program
                print("Exiting program successfully")
                break  # Exit the loop

            else:  # Invalid Option
                print("Invalid option, please choose again\n")


# Main entry point for the program
if __name__ == "__main__":
    auth_system = AuthenticationSystem()  # Create an instance of the AuthenticationSystem class
    auth_system.execute()  # Start the program
