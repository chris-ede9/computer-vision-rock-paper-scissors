# Computer Vision RPS

> The Computer Vision project utilises the solution Teachable Machine to process images, like Rock, Paper or Scissors hand gestures to determine the users choice. These inputs will be utilised within this project to play the rock, paper, scissors game against the computer.

## Milestone 1

- The first milestone introduced Teachable Machine and how it can process images, sounds or poses as classes to determine the end result. This is the link to the website: https://teachablemachine.withgoogle.com/
  
- Techable Machine was used to create 4 seperate classes - Rock, Paper, Scissors and Nothing to determine which gesture was chosen for the game. Using the webcam, the solution takes screeshots of different positions for each gesture to learn which you have picked. The more images taken, the better the outcome will be to decide which is taken. I did over 1000 images per class to get a decent result back.

- Once the classes are stored with multiple images, you then click to train the model. This can take a few minutes to process depending on how many images are stored per class. Once its finished training, you can then test the model to see how accurate it is. I had to do a few retraining exercises until I was happy it was at a good accuracy for the game.

> ![Alt text](Teachable%20Machine%20screenshot.png)

- Once happy with the model, you can export the project file for future amends and download as a Tensorflow model so that it can be used in a Python project. This will create a zip file with 2 files - keras_model.h5 and labels.txt. I have saved these files in the Rock, Paper, Scissors project git repo, ready for the next milestones to interact with the trained model for the game engine.

## Milestone 2

- This milestone was all about ensuring the environment was setup to be compatible for working with the tensorflow data that was created via Teachable machine.

- The following packages were required in the conda environment in order to run the code:
    - opencv-python
    - tensorflow
    - ipykernel
    
<br>

- Once the environment was setup, the code below was provided in order to run through the model to interpret this as percentages so it could be utilised in a later milestone:

```python
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```

## Milestone 3

- This milestone was all about creating the Rock, Paper, Scissors game in Python, simulating a user manual input and comparing this against a computer random input to confirm the result.

- The code was written in the file - manual_rps.py:

```python
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

def play():
    '''
    This fuction plays a single game of Rock, Paper, Scissors where the user picks an option and will print out the result against the computer's choice

    Returns:
        Nothing
    '''
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer selected {computer_choice}")
    get_winner(computer_choice, user_choice)

play()
```

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?