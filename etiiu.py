import random
number = random.randint(1, 100)
def guess_number():
    attempts = 0
    while True:
        try:
            guess  = int (input("Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            if guess < number:
                print("Too low! Try again.")
                attempts += 1
            elif guess > number:
                print("Too high! Try again.")
                attempts += 1
            else:
                attempts += 1
                print(f"Congratulations! You've guessed the number", number, "in", attempts, "attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_number()