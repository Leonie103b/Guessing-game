import art
import random

easy_attempt = 10
hard_attempt = 5




def set_difficult():
    choice_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()

    if choice_difficulty == "easy":
        return easy_attempt

    else:
        return hard_attempt



def compare(guess,computer_choice):
    if guess > computer_choice:
        print("Too high,guess again.")

    elif guess < computer_choice:
        print("Too low, guess again.")

    else:
        print(f"You win, the correct number is {computer_choice}")



def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game! \n"
          "I am thinking of a number between 1 and 100.")
    computer_choice = random.randint(0, 100)


    turns = set_difficult()

    guess = 0
    while guess != computer_choice:
        if turns < 1:
            print("You are out of attempts, you lose.")
            break
        else:
            print(f"You have {turns} attempts remaining to guess the numer")
            guess = int(input("Make a guess:"))
            compare(guess, computer_choice)
            turns -= 1



game()
