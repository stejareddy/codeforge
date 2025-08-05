# Rock Paper Sissors game 
import random 
def play_rps():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return play_rps()
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
if __name__ == "__main__":
    play_rps()
# To run the game, execute this script.
# You can play multiple rounds by calling play_rps() again.
# You can also modify the game to keep track of scores or play multiple rounds.
# To play again, simply call the function play_rps() again.
# You can also add more features like score tracking or best of three rounds.
# This is a simple implementation of the Rock, Paper, Scissors game.
# The game is interactive and allows the user to play against the computer.
# The game can be extended with more features like score tracking or best of three rounds.
# The game is designed to be simple and easy to play.
# The game can be played in the terminal or command line.
# The game is a fun way to practice Python programming and random number generation.                