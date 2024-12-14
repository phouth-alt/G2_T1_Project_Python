from register import register
#from reset import reset_pass
from login import login
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
                password = input("Enter password: ")
                reset_pass(username,password)
                print("\n")

            elif input_options == '4':
                print("\nLogin functionality is under development.\n")
                print("\n")

            elif input_options == '5':
                print("Exiting program successfuly")
                break
            else:
                print("invalid option, please choose options again\n")


if __name__ == "__main__":
    user1 = AuthenticationSystem()
    user1.Options()