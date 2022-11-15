import random

option = ["rock", "paper", "scissors"]
running = True

while running:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Rock, Paper or Scissors? (Enter rock / paper / scissors): ")

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose...")
    
    again = input("Wanna play again? (y/n): ").lower()
    
    if not again == "yes" or "y":
        running = False

print("alright thanks for playing")




