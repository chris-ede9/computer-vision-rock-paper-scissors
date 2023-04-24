import random
import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissors():

    def __init__(self) -> None:
        '''
        Initialises the game by setting up the keras data model and webcam feed. The play method is called until a winner is announced

        Returns:
            Nothing
        '''
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.user_name = self.get_user_name()
        self.play()
        
        while True:
            result = input("Would you like to play again? ")
            if result.lower() == 'n' or result.lower() == "no":
                break
            elif result.lower() == 'y' or result.lower() == "yes":
                self.play()
            else:
                print("I am unsure on your answer, please enter Yes or No")

        self.exit_game()

    def play(self) -> None:
        '''
        This fuction plays a single game of Rock, Paper, Scissors where the user picks an option and will print out the result against the computer's choice
        The winner is the first to win 3 rounds

        Returns:
            Nothing
        '''
        self.user_wins = 0
        self.computer_wins = 0

        while self.computer_wins < 3 and self.user_wins < 3:
            input("Press Enter when ready to the play the round")
            user_choice = self.get_prediction()
            computer_choice = self.get_computer_choice()
            print(f"User selected {user_choice}")
            print(f"Computer selected {computer_choice}")
            winner = self.get_winner(computer_choice, user_choice)

            if winner == "computer":
                self.computer_wins += 1
            elif winner == "user":
                self.user_wins += 1

        if self.computer_wins > self.user_wins:
            print("You lost the game")
        elif self.computer_wins < self.user_wins:
            print("You won the game!!!")

    def get_user_name(self) -> str:
        '''
        This function requests the User to enter their name

        Returns:
            str: User's name. If nothing entered, this defaults to "User"
        '''
        name = input("What is your name? ")
        if name == "":
            name = "User"
        return name

    def get_computer_choice(self):
        '''
        This function picks a random choice from the list containing "Rock", "Paper" or "Scissors"

        Returns:
            String: The random game choice from the computer
        '''
        options = ["Rock", "Paper", "Scissors"]
        return random.choice(options)

    def get_prediction(self):
        '''
        This function uses the keras models data to determine the user choice by a still image taken from the webcam. Multiple images are taken in a 5 second period.
        Once all images are captured, the choice of Rock, Paper, Scissors or Nothing is determined by the image that was selected the most. 

        Returns:
            String: The game choice from the user
        '''
        result = [0] * 4

        # Loop for 5 seconds, capturing the image choice index each time and adding it in the results array
        t_end = time.time() + 5.5
        while time.time() < t_end:
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            self.show_score_and_countdown(frame, int(t_end - time.time()))
            cv2.imshow('frame', frame)
            index_max = np.argmax(prediction)
            #store the result for that
            result[index_max] += 1

            if cv2.waitKey(1) == ord('q'):
                break

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

    def get_winner(self, computer_choice, user_choice) -> str:
        '''
        This function determines the winner of a Rock, Paper, Scissors game by comparing the computer choice and the user choice

        Returns:
            str: The Winner - "user", "computer" or "tie"
        '''
        if user_choice.lower() == "nothing":
            print("No user choice was selected")
            return "nothing"
        elif computer_choice.lower() == user_choice.lower():
            print("It is a tie!")
            return "tie"
        elif computer_choice.lower() == "rock":
            if user_choice.lower() == "scissors":
                print("You lost the round")
                return "computer"
            elif user_choice.lower() == "paper":
                print("You won the round!")
                return "user"
        elif computer_choice.lower() == "paper":
            if user_choice.lower() == "rock":
                print("You lost the round")
                return "computer"
            elif user_choice.lower() == "scissors":
                print("You won the round!")
                return "user"
        elif computer_choice.lower() == "scissors":
            if user_choice.lower() == "paper":
                print("You lost the round")
                return "computer"
            elif user_choice.lower() == "rock":
                print("You won the round!")
                return "user"
        else:
            print("Error occurred")
            
    def show_score_and_countdown(self, screenshot, time_left) -> None:
        '''
        This function prints the current score of the game in the top left corner of the webcam screen
        It also shows the count down to when th choice is selected in the right corner

        Returns:
            Nothing
        '''
        # Set the text attributes
        font = cv2.FONT_HERSHEY_COMPLEX
        scale = 1
        colour = (0, 0, 0)
        thickness = 3
        line_type = 2

        # User score
        cv2.putText(screenshot, f"{self.user_name } Score: {self.user_wins}", (0, 30), font, scale, colour, thickness, line_type)
        # Computer score
        cv2.putText(screenshot, f"Computer Score: {self.computer_wins}", (0, 60), font, scale, colour, thickness, line_type)
        # Countdown
        cv2.putText(screenshot, f"{time_left}", (600, 30), font, scale, colour, thickness, line_type)


    def exit_game(self) -> None:
        '''
        This fuction exits the game by releasing the cap object and destroying the windows

        Returns:
            Nothing
        '''
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

if __name__ == "__main__":
    new_game = RockPaperScissors()
