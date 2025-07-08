import random

def get_user_choice():
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter the number (1/2/3): ").strip()
    options = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    return options.get(choice, None)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    
    if winner == "tie":
        print("Result: It's a tie!")
    elif winner == "user":
        print("Result: You win! ")
    else:
        print("Result: Computer wins! ")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScores => You: {user_score} | Computer: {computer_score}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    print(" Welcome to Rock, Paper, Scissors!")
    play_game()
