import os
import random
from datetime import datetime
from Alphabet import *
from Password import Password


class Generator:
    def __init__(self, include_upper=False, include_lower=False, include_num=False, include_sym=False):
        self.alphabet = Alphabet(include_upper, include_lower, include_num, include_sym)

    def main_loop(self):
        print("\nHey There, Welcome to TAENTED Password Generator :)")
        self.print_menu()

        user_option = "-1"
        while user_option != "4":
            user_option = input("\nChoice: ").strip()

            if user_option == "1":
                self.request_password()
                self.print_menu()
            elif user_option == "2":
                self.check_password()
                self.print_menu()
            elif user_option == "3":
                self.print_useful_info()
                self.print_menu()
            elif user_option == "4":
                self.print_quit_message()
            else:
                print("\nKindly select one of the available commands")
                self.print_menu()

    def generate_password(self, length: int):
        chars = self.alphabet.get_alphabet()
        if not chars:
            raise ValueError("Alphabet is empty. Cannot generate password.")

        password = "".join(random.choice(chars) for _ in range(length))
        return Password(password)

    def print_useful_info(self):
        print("\nPassword Tips:")
        print("- Use at least 8 characters (the more, the better).")
        print("- Mix lowercase, uppercase, numbers, and symbols if possible.")
        print("- Create passwords randomly rather than guessing them yourself.")
        print("- Don't reuse the same password on different sites.")
        print("- Avoid names, dates, words, or predictable patterns.")


    def request_password(self):
        print("\nAnswer the following questions by Yes or No \n")

        include_lower = self.get_user_preference("Do you want Lowercase letters \"abcd...\" to be used?")
        include_upper = self.get_user_preference("Do you want Uppercase letters \"ABCD...\" to be used?")
        include_num = self.get_user_preference("Do you want Numbers \"1234...\" to be used?")
        include_sym = self.get_user_preference("Do you want Symbols \"!@#$...\" to be used?")

        if not (include_lower or include_upper or include_num or include_sym):
            print("You must select at least one character set.")
            return

        # Ask for password length
        length = 0
        while length <= 0:
            try:
                length = int(input("\nEnter password length: ").strip())
                if length <= 0:
                    print("Password length must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        generator = Generator(include_upper, include_lower, include_num, include_sym)
        password = generator.generate_password(length)
        print(f"\nYour generated password -> {password}")

        site_name = input("\nWrite down the name of Site for future reference: ").strip()
        timestamp = datetime.now().strftime("%H-%M %p %d-%B-%Y")
        filename = os.path.expanduser(f"~/Desktop/Generated_password({timestamp}).txt")

        try:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"\nName of Site: {site_name}\nPassword Generated: {password}\nDate & Time: {timestamp}\n")
            print(f"Generated Password saved successfully to {filename}!")
        except Exception as e:
            print(f"Failed to save password: {e}")

    def get_user_preference(self, message: str) -> bool:
        while True:
            choice = input(f"{message} (Type 'Yes' or 'No'): ").strip().lower()
            if choice == "yes":
                return True
            elif choice == "no":
                return False
            else:
                print("Invalid input. Please answer with 'Yes' or 'No'.")

    def check_password(self):
        pw = input("\nEnter your password: ").strip()
        password_obj = Password(pw)
        print(password_obj.evaluate_strength())

    def print_menu(self):
        print("\nMenu Options:")
        print("Enter 1 - Password Generator")
        print("Enter 2 - Password Strength Check")
        print("Enter 3 - Useful Information")
        print("Enter 4 - Quit")

    def print_quit_message(self):
        print("\nClosing program....\nProgram Closed.")


if __name__ == "__main__":
    app = Generator()
    app.main_loop()
