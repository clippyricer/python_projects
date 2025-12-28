# This is a quiz game :D
```

# Modules
import time
from random import randint
from questions import questions
from answers import answers

score = 0

print("Welcome to BLANES QUIZ SHOW!!!")

play = input("Would you like to play? (y/n:) ")

if play != "y":
    print("Good bye!")
    exit

print("Make sure you speel corectly in LOWERCASE (names can be either)")

# Print score function
# Change is either gained or lost
# gl is the number that you either gained or lost
def show_score(change, gl):
    print(f"You {change} {gl} points!")
    print(f"Your score is currently {score}")


# Random num
ran_num = randint(0, 5)

# Actual questions
def question():
    print(questions[ran_num])
    answer = input()
    if answer == answers[ran_num]:
        score = score + 1
        print("Correct!")
        print("+1pt")
        show_score("gained", 1)
    else:
        score = score + 1
        print("Incorrect!")
        print("-1pt")
        show_score("lost", 1)

# Outputs question
question()
question()
question()
question()
question()
```
