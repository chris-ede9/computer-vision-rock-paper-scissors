import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    # Returns a random value from the choices list
    return random.choice(choices)

def get_user_choice():
    '''
    This fuction asks the user to select Rock, Paper or Scissors and validates the request until its valid

    Returns:
        String: "Rock", "Paper" or "Scissors"
    '''
    while True:
        choice = input("Please select Rock, Paper or Scissors ")
        if choice.lower() in choices:
            return choice
        else:
            print("Invalid choice picked!")
