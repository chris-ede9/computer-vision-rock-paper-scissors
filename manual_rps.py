import random

def get_computer_choice():
    # Returns a random value from the choices list
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
