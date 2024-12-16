from register import register  # Module to handle user registration
from reset import reset_pass  # Module to handle password reset functionality
from login import login  # Module to handle user login functionality
from forget import recover_password  # Module for password recovery
from generateOTP import generate_alphanumeric_otp  # Function to generate secure OTP
from update_password import update_password  # Module to update user's password
from encrypt_password import encrypt_password  # Function to encrypt passwords
from password_strength import pass_strength  # Function to check password strength

# Main class for the authentication system
class AuthenticationSystem:
    # Menu-driven options method
    def Options(self):
        # Infinite loop to keep the menu running until the user exits
        while True:
            # Display the menu options
            print("--------------------------------------------")
            print("-----------Authentication System------------")
            print("--------------------------------------------")
            print("1.Login")  # Login option
            print("2.Register")  # Registration option
            print("3.Reset Password")  # Reset password option
            print("4.Forget Password")  # Password recovery option
            print("5.Exit program")  # Exit the program
            print("--------------------------------------------")
            print("-------------Enter an option----------------")
            print("--------------------------------------------")
            
            # Get the user's choice
            input_options = input("").strip()
            
            # Option 1: Login
            if input_options == '1':
                username = input("Username: ").strip()  # Input for username
                password = input("Enter password:").strip()  # Input for password
                # Call the login function and check if it succeeds
                if login(username, password):
                    print("Login successfully")  # Success message
                else:
                    print("Login again")  # Failure message
                print("\n")  # Blank line for spacing
            
            # Option 2: Register
            elif input_options == '2':
                username = input("Username: ").strip()  # Input for username
                password = input("Enter password: ").strip()  # Input for password
                phone = input("Phone number: ").strip()  # Input for phone number
                # Call the register function
                register(username, password, phone)
                print("\n")  # Blank line for spacing
            
            # Option 3: Reset Password
            elif input_options == '3':
                username = input("Enter username: ").strip()  # Input for username
                phone = input("Phone number: ").strip()  # Input for phone number
                password = input("Enter current password: ").strip()  # Input for current password
                new_password = input("Enter new password: ").strip()  # Input for new password
                # Call the reset_pass function
                reset_pass(username, password, phone, new_password)
                print("\n")  # Blank line for spacing
            
            # Option 4: Forget Password
            elif input_options == '4':
                phone = input("Phone number: ").strip()  # Input for phone number
                # Call the recover_password function
                if recover_password(phone):  # If recovery is successful
                    otp = generate_alphanumeric_otp()  # Generate a secure OTP
                    print("Your secure alphanumeric OTP is: {}".format(otp))  # Display OTP
                    input_OTP = input("Enter your OTP: ").strip()  # Input for OTP
                    # Check if the entered OTP matches the generated OTP
                    if input_OTP == otp:
                        new_password = input("New password: ").strip()  # Input for new password
                        # Check the strength of the new password
                        if pass_strength(new_password):
                            new_password = encrypt_password(new_password)  # Encrypt the new password
                            update_password(phone, new_password)  # Update the password in the system
                else:
                    print("You don't have an account yet.")  # Error message for invalid phone number
                print("\n")  # Blank line for spacing
            
            # Option 5: Exit Program
            elif input_options == '5':
                print("Exiting program successfully")  # Exit message
                break  # Break the loop to exit the program
            
            # Invalid Option
            else:
                print("Invalid option, please choose again\n")  # Error message for invalid input

# Main entry point for the program
if __name__ == "__main__":
    user1 = AuthenticationSystem()  # Create an instance of the AuthenticationSystem class
    user1.Options()  # Call the Options method to start the program
