import random

option = ["rock", "paper", "scissors"]
running = True

while running:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Rock, Paper or Scissors? (Enter rock / paper / scissors): ")

    print(f"\nYou: {player}")
    print(f"Computer: {computer}\n")

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
    
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("\nAlright thanks for playing")
print("\nSource Code: \nhttps://github.com/yin070406/simple_python_project/tree/rock-paper-scissors")




