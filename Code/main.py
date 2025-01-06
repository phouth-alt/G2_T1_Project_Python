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
            print("\t--------------------------------------------")
            print("\t-----------Authentication System------------")
            print("\t--------------------------------------------")
            print("\t1.Register")  # Registration option
            print("\t2.Login")  # Login option
            print("\t3.Reset Password")  # Reset password option
            print("\t4.Forget Password")  # Password recovery option
            print("\t5.Exit program")  # Exit the program
            print("\t--------------------------------------------")
            print("\t-----------Enter an option(1-5)-------------")
            print("\t--------------------------------------------")

            
            # Get the user's choice
            input_options = input("\t:").strip()
            
             # Option 1: Register
            if input_options == '1':
                print("\t--------------------------------------------")
                print("\t---------------Create account---------------")
                print("\t--------------------------------------------")
                username = input("\tUsername: ").strip()  # Input for username
                password = input("\tEnter password: ").strip()  # Input for password
                phone = input("\tPhone number: ").strip()  # Input for phone number
                # Call the register function
                register(username, password, phone)
                print("\n")  # Blank line for spacing
            
            # Option 2: Login
            elif input_options == '2':
                print("\t--------------------------------------------")
                print("\t----------------login account---------------")
                print("\t--------------------------------------------")
                username = input("\tUsername: ").strip()  # Input for username
                password = input("\tEnter password:").strip()  # Input for password
                # Call the login function and check if it succeeds
                if login(username, password):
                    print("\tLogin successfully")  # Success message
                else:
                    print("\tLogin again")  # Failure message
                print("\n")  # Blank line for spacing
            
            # Option 3: Reset Password
            elif input_options == '3':
                print("\t--------------------------------------------")
                print("\t---------------Reset password---------------")
                print("\t--------------------------------------------")
                username = input("\tEnter username: ").strip()  # Input for username
                phone = input("\tPhone number: ").strip()  # Input for phone number
                password = input("\tEnter current password: ").strip()  # Input for current password
                new_password = input("\tEnter new password: ").strip()  # Input for new password
                # Call the reset_pass function
                reset_pass(username, password, phone, new_password)
                print("\n")  # Blank line for spacing
            
            # Option 4: Forget Password
            elif input_options == '4':
                print("\t--------------------------------------------")
                print("\t--------------Recover password--------------")
                print("\t--------------------------------------------")
                phone = input("\tPhone number: ").strip()  # Input for phone number
                # Call the recover_password function
                if recover_password(phone):  # If recovery is successful
                    otp = generate_alphanumeric_otp()  # Generate a secure OTP
                    print("\tYour secure alphanumeric OTP is: {}".format(otp))  # Display OTP
                    input_OTP = input("\tEnter your OTP: ").strip()  # Input for OTP
                    # Check if the entered OTP matches the generated OTP
                    if input_OTP == otp:
                        new_password = input("\tNew password: ").strip()  # Input for new password

                        # Check the strength of the new password
                        if pass_strength(new_password):
                            new_password = encrypt_password(new_password)  # Encrypt the new password
                            update_password(phone, new_password)  # Update the password in the system
                    else:
                        print("\tincorrect OTP")
                else:
                    print("\tYou don't have an account yet.")  # Error message for invalid phone number
                print("\n")  # Blank line for spacing
            
            # Option 5: Exit Program
            elif input_options == '5':
                print("\tExiting program successfully")  # Exit message
                break  # Break the loop to exit the program
            
            # Invalid Option
            else:
                print("\tInvalid option, please choose again\n")  # Error message for invalid input

# Main entry point for the program
if __name__ == "__main__":
    user1 = AuthenticationSystem()  # Create an instance of the AuthenticationSystem class
    user1.Options()  # Call the Options method to start the program
