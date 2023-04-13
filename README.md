# Computer Vision RPS

> The Computer Vision project utilises the solution Teachable Machine to process images, like Rock, Paper or Scissors hand gestures to determine the users choice. These inputs will be utilised within this project to play the rock, paper, scissors game against the computer.

## Milestone 1

- The first milestone introduced Teachable Machine and how it can process images, sounds or poses as classes to determine the end result. This is the link to the website: https://teachablemachine.withgoogle.com/
  
- Techable Machine was used to create 4 seperate classes - Rock, Paper, Scissors and Nothing to determine which gesture was chosen for the game. Using the webcam, the solution takes screeshots of different positions for each gesture to learn which you have picked. The more images taken, the better the outcome will be to decide which is taken. I did over 1000 images per class to get a decent result back.

- Once the classes are stored with multiple images, you then click to train the model. This can take a few minutes to process depending on how many images are stored per class. Once its finished training, you can then test the model to see how accurate it is. I had to do a few retraining exercises until I was happy it was at a good accuracy for the game.

> ![Alt text](Teachable%20Machine%20screenshot.png)

- Once happy with the model, you can export the project file for future amends and download as a Tensorflow model so that it can be used in a Python project. This will create a zip file with 2 files - keras_model.h5 and labels.txt. I have saved these files in the Rock, Paper, Scissors project git repo, ready for the next milestones to interact with the trained model for the game engine.

## Milestone 2

- Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:

```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?