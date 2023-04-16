import random

def get_computer_choice():
    # Returns a random value from the options list
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_user_choice():
    '''
    This fuction asks the user to select Rock, Paper or Scissors and validates the request until its valid

    Returns:
        String: "Rock", "Paper" or "Scissors"
    '''
    options = ["rock", "paper", "scissors"]
    while True:
        choice = input("Please select Rock, Paper or Scissors ")
        if choice.lower() in options:
            return choice
        else:
            print("Invalid choice picked!")

def get_winner(computer_choice, user_choice):
    '''
    This fuction determines the winner of a Rock, Paper, Scissors game by comparing the computer choice and the user choice

    Returns:
        Nothing
    '''
    if computer_choice.lower() == user_choice.lower():
        print("It is a tie!")
    elif computer_choice.lower() == "rock":
        if user_choice.lower() == "scissors":
            print("You lost")
        elif user_choice.lower() == "paper":
            print("You won!")
    elif computer_choice.lower() == "paper":
        if user_choice.lower() == "rock":
            print("You lost")
        elif user_choice.lower() == "scissors":
            print("You won!")
    elif computer_choice.lower() == "scissors":
        if user_choice.lower() == "paper":
            print("You lost")
        elif user_choice.lower() == "rock":
            print("You won!")
    else:
        print("An error occured")
