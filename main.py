"""
Main python file
"""

from user import User
from utils import display_message, print_star


def main():
    # Loop until user want to exit
    while True:
        print_star()
        print(
            """
        \t\t\t Welcome to Insight Workshop Academy

        \tPlease Choose One of these options:

        \t\t1) Register
        \t\t2) Login
        \t\t3) Quit

        """
        )

        try:
            # Check for valid user input
            user_choose = int(input("\t\tPlease Choose 1, 2 or 3 :  "))
        except:
            display_message("Please Enter Valid Integer value.")
            continue

        user = User()
        if user_choose == 1:
            wrong_data = True
            # Loop until user provide correct data
            while wrong_data:
                user_data = user.register()
                display_message(message=user_data["message"])
                if user_data["user"]:
                    wrong_data = False

        elif user_choose == 2:
            wrong_data = True
            # Loop until user provide correct Data
            while wrong_data:
                user_data = user.login()
                display_message(message=user_data["message"])
                if user_data["user"]:
                    # Loop until user want to exit
                    while True:
                        wrong_data = False
                        print(
                            f"""
                        \t\t\t Welcome {user.email} to Insight Workshop Academy

                        \tPlease Choose One of these options:

                        \t\t1) View Details
                        \t\t2) Change Password
                        \t\t3) Delete User
                        \t\t4) Logout
                        """
                        )
                        try:
                            login_user_choice = int(
                                input("\t\tPlease Choose 1, 2, 3 or 4:  ")
                            )
                        except:
                            display_message("Please Enter Valid Integer value.")
                            continue

                        if login_user_choice == 1:
                            user.show_details()

                        elif login_user_choice == 2:
                            user.change_password()

                        elif login_user_choice == 3:
                            user.delete_user()
                            break

                        elif login_user_choice == 4:
                            break

                        else:
                            display_message(message="Please Enter Valid Option value.")
                            continue
        elif user_choose == 3:
            display_message(message="Thank you for using our app.")
            break

        else:
            display_message(message="Please Enter Valid Option value.")
            continue


if __name__ == "__main__":
    main()
