"""
Some simple utils functions which are used many times 
"""
import re


def print_star() -> None:
    print("\n", "* " * 50, "\n")


def display_message(message: str) -> None:
    print_star()
    print(f"\t\t\t{message}")
    print_star()


def input_user_details(type: str) -> tuple[str]:
    print_star()
    print(
        f"""

    \t\t Please Enter Email and Password for {type}

    """
    )

    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    email = input("\t\t\tEmail Address :  ")
    while not re.fullmatch(email_pattern, email):
        print("\n\n\t\t\tPlease Enter Valid Email Address.\n\n")
        email = input("\t\t\tEmail Address :  ")

    password = input("\t\t\tPassword :  ").strip()
    password_pattern = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,14}$"
    )
    while not re.fullmatch(password_pattern, password):
        print(
            "\n\n\t\t\tPassword should be between 8-14 chracter and should contain atleast 1 Captital letter, Number and Special Characters.\n\n"
        )
        password = input("\t\t\tPassword :  ").strip()
    return (email, password)
