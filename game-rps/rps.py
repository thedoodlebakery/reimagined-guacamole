# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
import random

# Player Inputs
playerOne = input("Do you choose rock, paper or scissors? \n");
playComputer = input("Do you want to play with the computer? \n");

computerPlayer = ""


def computerChoice():
    computerAnswer = ["rock", "paper", "scissors"];
    global computerPlayer;
    computerPlayer = random.choice(computerAnswer);
    print ("Player two answers: \n" + computerPlayer);

if playComputer == 'yes':
    computerChoice();
    global playerTwo;
    playerTwo = computerPlayer
    #print (playComputer)
else:
    playerTwo = input("Do you choose rock, paper or scissors? \n");
    
    

def game():
    # playerTwo = computerPlayer;
    if (playerOne == "rock" and playerTwo == "paper") | (playerOne == "scissors" and playerTwo == "rock") | (playerOne == "paper" and playerTwo == "scissors"):
        print("Player Two wins!");
    elif (playerOne == "paper" and playerTwo == "rock") | (playerOne == "rock" and playerTwo == "scissors") | (playerOne == "scissors" and playerTwo == "paper"):
        print("Player One wins!");
    elif playerOne == playerTwo:
        print("It's a draw!");
    else:
        print("Please check your answer and try again.");

game();
   


