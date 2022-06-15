"""
User functions such as login, register, change password and detail information
"""
from __future__ import annotations
import fileinput
from os import path

from mail import SendEmail
from thread import EmailThread
from utils import input_user_details, print_star


class User:
    def __init__(self) -> None:
        # if user.txt file doesn't exist then create it
        if not path.exists("user.txt"):
            open("user.txt", "a").close()
        self.email: str
        self.password: str

    def check_email(self) -> User | None:
        """Check if user with given email already exists or not"""

        with open("user.txt", "r") as file:
            data = file.readlines()
            for user_data in data:
                if self.email == user_data.strip().split(",")[0]:
                    return self
            return

    def check_user(self) -> User | None:
        """check if user with email and password exists or not"""

        with open("user.txt", "r") as file:
            data = file.readlines()
            user_data = [self.email, self.password]
            for u_data in data:
                if user_data == u_data.strip().split(","):
                    return self
            return

    def login(self):
        """Simple Login by checking if email and password is valid or not"""

        (self.email, self.password) = input_user_details(type="Login")

        if self.check_user():
            return {"user": self, "message": "Log in Successfully"}

        return {"user": None, "message": "Please Enter Correct Data."}

    def register(self) -> User | None:
        """Simple register by checking if email is already registered or not"""

        (self.email, self.password) = input_user_details(type="Register")

        if self.check_email():
            return {"user": None, "message": "User with this email already exists"}

        user_data = f"{self.email},{self.password}\n"

        with open("user.txt", "a") as file:
            file.write(user_data)
            # Sending user registered email using thread
            EmailThread(send_email=SendEmail(), user=self).start()
            file.close()

        return {"user": self, "message": "Registerd Successfully."}

    def show_details(self) -> None:
        """Showing User Email and Password"""

        print_star()
        print(
            f"""

        \t\t\tYour Email : {self.email}
        \t\t\tYour Password : {self.password}

        """
        )
        print_star()
        input("\t\t\tPress any key to go back: ")

    def delete_user(self) -> None:
        """Delete User details from the file"""

        print_star()
        print(
            f"""

        \t\t\tAre you sure you want to delete your account?

        """
        )

        input_data = input("\t\t\tPlease Press Y for Yes: ").lower()

        if input_data == "y":
            user_email_password = f"{self.email},{self.password}\n"
            with fileinput.FileInput("user.txt", inplace=True, backup=".bak") as file:
                for line in file:
                    print(line.replace(user_email_password, ""), end="")
                file.close()
            del self

    def change_password(self):
        """Change user password in the file"""

        print_star()
        print(
            f"""

        \t\t\tAre you sure you want to change your Password? 

        """
        )

        input_data = input("\t\t\tPlease Press Y for Yes: ").lower()

        if input_data == "y":
            print_star()
            new_password = input("\n\t\t\tPlease Enter New Password : ")
            old_email_password = f"{self.email},{self.password}\n"
            new_email_password = f"{self.email},{new_password}\n"
            with fileinput.FileInput("user.txt", inplace=True, backup=".bak") as file:
                for line in file:
                    print(line.replace(old_email_password, new_email_password), end="")
                file.close()
            self.password = new_password
