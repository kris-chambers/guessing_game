import random

MIN = 0
MAX = 3

def main_loop():
    game_running = True
    
    while game_running:
        prompt = f"\nPlease choose a number between {MIN} and {MAX}:"
        prompt += "\nEnter 'quit' to end the program. "
        computer_generated_number = random.randint(MIN, MAX)
        user_guess = input(prompt)
        if user_guess == "quit":
            game_running = False
        elif int(user_guess) < MIN:
            print(f"Your guess is less than {MIN}. Please try again.")
            continue
        elif int(user_guess) > MAX:
            print(f"Your guess is greater than {MAX}. Please try again.")
            continue
        elif int(user_guess) == computer_generated_number:
            print("That is the correct number! You win!")
            continue
        else:
            print("That is not the correct number. You lose.")
            continue 
    
if __name__ == '__main__':
    main_loop()  