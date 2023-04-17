import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    '''
    This fuction picks a random choice from the list containing "Rock", "Paper" or "Scissors"

    Returns:
        String: The random game choice from the computer
    '''
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_prediction():
    '''
    This fuction uses the keras models data to determine the user choice by a still image taken from the webcam


    Returns:
        String: The game choice from the user
    '''
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    result = [0] * 4

    # Loop for 5 seconds, capturing the image choice index each time and adding it in the results array
    t_end = time.time() + 5
    while time.time() < t_end:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        index_max = np.argmax(prediction)
        result[index_max] += 1

    # Get the max value from the result array
    index_max = np.argmax(result)
    # The index determines which choice to return based on the labels.txt file
    if index_max == 0:
        return "Rock"
    elif index_max == 1:
        return "Paper"
    elif index_max == 2:
        return "Scissors"
    else:
        return "Nothing"
    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def get_winner(computer_choice, user_choice):
    '''
    This fuction determines the winner of a Rock, Paper, Scissors game by comparing the computer choice and the user choice

    Returns:
        Nothing
    '''
    if user_choice.lower() == "nothing":
        print("No user choice was selected")
    elif computer_choice.lower() == user_choice.lower():
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
        print("Error occurred")

def play():
    '''
    This fuction plays a single game of Rock, Paper, Scissors where the user picks an option and will print out the result against the computer's choice

    Returns:
        Nothing
    '''
    user_choice = get_prediction()
    computer_choice = get_computer_choice()
    print(f"User selected {user_choice}")
    print(f"Computer selected {computer_choice}")
    get_winner(computer_choice, user_choice)

play()