"""
Some simple utils functions which are used many times 
"""


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

    email = input("\t\t\tEmail Address :  ")
    password = input("\t\t\tPassword :  ")
    return (email, password)
