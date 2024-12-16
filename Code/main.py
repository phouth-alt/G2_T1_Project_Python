from register import register
from reset import reset_pass
from login import login
from forget import recover_password
from generateOTP import generate_alphanumeric_otp
from update_password import update_password
class AuthenticationSystem:
    def Options(self):
        while True:
            print("--------------------------------------------")
            print("-----------Authentication System------------")
            print("--------------------------------------------")
            print("1.Login")
            print("2.Register")
            print("3.Reset Password")
            print("4.ForgetPassword")
            print("5.Exit program")
            print("--------------------------------------------")
            print("-------------Enter an option----------------")
            print("--------------------------------------------")
            input_options = input("")
            if input_options == '1':
                username = input("Username: ").strip()
                password = input("Enter password:").strip()
                if login(username,password):
                   print("Login successfully")
                else:
                    print("Login agian")
                print("\n")
            elif input_options == '2':
                username = input("username : ")
                password = input("Enter password:").strip()
                phone = input("phone number: ").strip()
                register(username,password,phone)
                print("\n")
              
            elif input_options == '3':
                username = input("Enter username: ")
                phone = input("phone number : ")
                password = input("Enter current password: ")
                new_password = input("Enter new password:")
                reset_pass(username,password,phone,new_password)
                print("\n")

            elif input_options == '4':
                phone = input("phone number :")
                if recover_password(phone):
                    generate_alphanumeric_otp
                    input_OTP = input("Enter your OTP: ")
                    if input_OTP == generate_alphanumeric_otp:
                        new_password = input("new password: ")
                        update_password(phone,new_password)
                else:
                    print("you didn't have account yet.")
                print("\n")

            elif input_options == '5':
                print("Exiting program successfuly")
                break
            else:
                print("invalid option, please choose options again\n")


if __name__ == "__main__":
    user1 = AuthenticationSystem()
    user1.Options()