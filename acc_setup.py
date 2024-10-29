import os
from getpass import getpass  # To hide password input

def is_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    has_special = any(char in special_characters for char in password)
    return has_upper and has_lower and has_digit and has_special

def is_valid_username(username, existing_usernames):
    if len(username) < 4:
        print("Username must be at least 4 characters long.")
        return False
    elif username in existing_usernames:
        print("Username already exists. Please choose a different one.")
        return False
    return True

def load_existing_usernames(filepath):
    try:
        with open(filepath, "r") as file:
            # Split by `:` assuming username:password format in each line
            return {line.split(":")[0].strip() for line in file if line.strip()}
    except FileNotFoundError:
        print("Accounts file not found. Creating a new one.")
        open(filepath, "w").close()  # Create the file if it doesn't exist
        return set()

def save_account(username, password, filepath):
    try:
        with open(filepath, "a") as file:
            file.write(f"{username}:{password}\n")
        print("Your account has been successfully created!")
    except IOError:
        print("Error saving account. Please try again later.")

# Main program
def create_account():
    print("-----------------------------------")
    print("Rock, Paper, Scissors Account Setup")
    print("Version 1.0")
    print("-----------------------------------\n")

    filepath = "accounts.txt"
    existing_usernames = load_existing_usernames(filepath)

    while True:
        username = input("Pick a username (minimum 4 characters): ")
        if not is_valid_username(username, existing_usernames):
            continue

        password = getpass("Pick a password: ")
        if not is_strong_password(password):
            print("Password must be at least 8 characters, contain an uppercase letter, lowercase letter, number, and special character.")
            continue

        password_confirm = getpass("Confirm your password: ")
        if password != password_confirm:
            print("Passwords do not match. Please try again.")
            continue

        save_account(username, password, filepath)
        break

create_account()