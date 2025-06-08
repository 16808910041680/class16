import random
# Rock paper scissors game
def play_rps():
    user_input = input("Enter rock, paper, or scissors: ").lower()
    choices = ["rock", "paper", "scissors"]
    if user_input not in choices:
        print("Invalid choice. Please try again.")
        return play_rps()
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_input == computer_choice:
        if computer_choice == "rock":
            print("It's a tie! Both chose rock.")
        if computer_choice == "paper":
            print("It's a tie! Both chose paper.")
        if computer_choice == "scissors":
            print("It's a tie! Both chose scissors.")
    elif (user_input == "rock" and computer_choice == "scissors"):
        print("You win! Rock crushes scissors.")
    elif (user_input == "paper" and computer_choice == "rock"):
        print("You win! Paper covers rock.")
    elif (user_input == "scissors" and computer_choice == "paper"):
        print("You win! Scissors cut paper.")
    elif (user_input == "rock" and computer_choice == "paper"):
        print("You lose! Paper covers rock.")
    elif (user_input == "paper" and computer_choice == "scissors"):
        print("You lose! Scissors cut paper.")
    elif (user_input == "scissors" and computer_choice == "rock"):
        print("You lose! Rock crushes scissors.")
    else:
        print("Unexpected error occurred.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        return play_rps()
    elif play_again == "no":
        print("Thanks for playing!")
    else:
        print("Invalid input. Exiting the game.")
        return
play_rps()


