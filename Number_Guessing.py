import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")
print("Type 'q' to quit anytime.\n")

while is_running:
    user_input = input("Enter your guess: ").strip().lower()

    if user_input == "q":
        print("You quit the game. Goodbye!")
        break

    if not user_input.isdigit():
        print("Invalid guess. Please enter a whole number.")
        continue

    guess = int(user_input)
    guesses += 1

    if guess < lowest_num or guess > highest_num:
        print("That number is out of range.")
        print(f"Please select a number between {lowest_num} and {highest_num}.")
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:  
        print(f"Correct! The answer was {answer}.")
        print(f"Number of guesses: {guesses}")
        is_running = False
