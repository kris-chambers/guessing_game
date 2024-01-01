import random
import csv
import os
from datetime import datetime

MIN = 0
MAX = 3


def main_loop():
    game_running = True
    user_wins = 0
    computer_wins = 0
    filename = "stat.csv"
    current_datetime = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    while game_running:
        prompt = f"\nPlease choose a number between {MIN} and {MAX}:"
        prompt += "\nEnter 'quit' to end the program. "
        
        computer_generated_number = random.randint(MIN, MAX)
        user_guess = input(prompt)
            
        if user_guess == "quit":
            with open('stat.csv') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                total_user_wins = 0
                total_computer_wins = 0
                for row in csv_reader:
                    if row[1] == "USER":
                        total_user_wins +=1
                    else:
                        total_computer_wins += 1
                winning_percentage = round(((total_user_wins / 
                                          total_computer_wins) * 100), 2)        
                print("\nFinal Score")
                print(f"User Wins This Round: {user_wins}")
                print(f"Computer Wins This Round: {computer_wins}\n")
                print(f"User Wins Alltime: {total_user_wins}")
                print(f"Computer Wins Alltime: {total_computer_wins}\n")
                print("Your alltime winning percentage is"\
                                f" {winning_percentage}%. ")
                csvfile.close()
            
            
            game_running = False
        elif user_guess.isdigit():
            if int(user_guess) < MIN:
                print(f"Your guess is less than {MIN}. Please try again.")
                continue
            elif int(user_guess) > MAX:
                print(f"Your guess is greater than {MAX}. Please try again.")
                continue
            elif int(user_guess) == computer_generated_number:
                winner = "USER"
                user_wins += 1
                
                print("That is the correct number! You win!")
                
                if os.path.exists(filename):
                    with open(filename, 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([current_datetime, winner, 
                                        computer_generated_number ])
                else:
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(['DATE_TIME', 'WINNER', 
                                'WINNING_NUM(computer gen random number)'])
                        writer.writerow([current_datetime, winner,
                                        computer_generated_number])
                        csvfile.close()
                continue
            else:
                winner = "COMPUTER"
                computer_wins += 1
                
                print("That is not the correct number. You lose.")
                
                if os.path.exists(filename):
                    with open(filename, 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([current_datetime, winner,
                                        computer_generated_number])
                else:
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(['DATE_TIME', 'WINNER', 
                                'WINNING_NUM(computer gen random number)'])
                        writer.writerow([current_datetime, winner,
                                        computer_generated_number])
                        csvfile.close()
                continue
        else:
            print("That is not an integer. Please try again.")
            continue

if __name__ == '__main__':
    main_loop()  