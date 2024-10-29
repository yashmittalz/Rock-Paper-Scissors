import time
import random
import os

print("Developed by Yash Mittal. \nVisit https://yashmittalz.github.io for more projects. \n")
print("Version 1.0")
loose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
drew = 0
computer_lives = 7
password_list = []

def display_rules():
    print("*******************************")
    print("             RULES             ")
    print("*******************************")
    print("-Rock looses against Paper")
    print("-Rock beats Scissors")
    print("-Paper beats Rock")
    print("-Paper looses against Scissors")
    print("-Scissors beats Paper")
    print("-Scissors looses against Rock")
    print("*******************************")

def end_game():
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Game Over!")

def get_user_choice():
    while True:
        rps = input("Rock, Paper, Scissors?     ").lower()
        if rps in ["rock", "paper", "scissors", "!help", "!lives", "!score", "!drew", "exit"]:
            return rps
        else:
            print("Invalid choice. Please choose Rock, Paper, Scissors, or a command.")

def determine_winner(rps, computer):
                    if rps == computer:
                        return "draw"
                    elif    (rps == "rock" and computer == "scissors") or \
                        (rps == "paper" and computer == "rock") or \
                        (rps == "scissors" and computer == "paper"):
                        return "win"
                    elif (rps == "rock" and computer == "paper") or \
                        (rps == "paper" and computer == "scissors") or \
                        (rps == "scissors" and computer == "rock"):
                        return "lose"

while True:
    print("----------------------------------------")
    print("To begin fill in the below information.")
    print("----------------------------------------\n")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    with open("accounts.txt", "r") as searchfile:
        # Read accounts and check for valid username and password
        password_list = [line.strip().split(":") for line in searchfile]  # Split lines into username and password
        # Check if the entered username and password match any entry
        if any(user == username and pwd == password for user, pwd in password_list):
            print("----------------------------------------")
            print("Access Granted")
            time.sleep(0.5)
            print("Loading.")
            time.sleep(0.5)
            print("Loading..")
            time.sleep(0.5)
            print("Loading...\n")
            time.sleep(0.5)
            print("Rules")
            print("----------------------------------------")
            print("You start with",lives,"lives")
            print("If you win you get an extra life.")
            print("If you loose you loose a life.")
            print("If you draw, the lives stay the same")
            print("The computer has lives as well.")
            print("----------------------------------------")
            print("How to win? Type '!help'")
            print("Stop playing? Type 'exit'")
            print("Lives check? Type '!lives'")
            print("Draw check? Type '!drew'") 
            print("Score check? Type '!score'") 
            print("----------------------------------------")         
            time.sleep(1)
            print("Good Luck!!")

            # Start of the game
            while True:
                rps = get_user_choice()
                computer = random.choice(["rock", "paper", "scissors"])

                if rps == "!help":
                    display_rules()
                elif rps == "!lives":
                    print("remaining lives: ",lives)
                elif rps == "!score":
                    print("Your score: ", score)
                elif rps == "!drew":
                    print("You have drawn: ",drew, "times")
                else:
                    result = determine_winner(rps, computer)

                    if result == "win":
                        print(f"The computer chose {computer}. You win!")
                        score += 1
                    elif result == "lose":
                        print(f"The computer chose {computer}. You lose!")
                        lives -= 1
                    else:
                        print(f"The computer chose {computer}. It's a draw!")
                        drew +=1

                    # Display current score and lives
                    print(f"Score: {score}, Lives: {lives}")

                if lives == 0 or computer_lives == 0:
                    end_game()
                    print(f"You got {score} correct and drew {drew} times.")
                    input("Press enter to exit.")
                    exit()
                #exit
                if rps == "exit":
                    break 
        else:
            print("\nYour username or password is incorrect.")
            break