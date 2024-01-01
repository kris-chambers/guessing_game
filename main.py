import random

MIN = 0
MAX = 3


def main_loop():
    game_running = True
    user_wins = 0
    computer_wins = 0
    
    while game_running:
        prompt = f"\nPlease choose a number between {MIN} and {MAX}:"
        prompt += "\nEnter 'quit' to end the program. "
        
        computer_generated_number = random.randint(MIN, MAX)
        user_guess = input(prompt)
            
        if user_guess == "quit":
            print("\nFinal Score")
            print(f"User Wins: {user_wins}")
            print(f"Computer Wins: {computer_wins}\n")
            game_running = False
        elif user_guess.isdigit():
            if int(user_guess) < MIN:
                print(f"Your guess is less than {MIN}. Please try again.")
                continue
            elif int(user_guess) > MAX:
                print(f"Your guess is greater than {MAX}. Please try again.")
                continue
            elif int(user_guess) == computer_generated_number:
                print("That is the correct number! You win!")
                user_wins += 1
                continue
            else:
                print("That is not the correct number. You lose.")
                computer_wins += 1
                continue
        else:
            print("That is not an integer. Please try again.")
            continue
    
if __name__ == '__main__':
    main_loop()  