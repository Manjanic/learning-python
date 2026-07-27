import random
choices = ["rock", "paper", "scissors"]
wins = 0
losses = 0
ties = 0
while True:
    playerChoice = input("Enter your choice (rock/paper/scissors) or quit  ").lower()
    if playerChoice == "quit":
        break
    if playerChoice not in choices:
        print("Invalid choice! Type rock, paper, or scissor")
        continue
    computerChoice = random.choice(choices)
    print(f"computer chose {computerChoice}")
    if playerChoice == computerChoice:
        print("it's a tie")
        ties += 1
    elif(playerChoice ==  "rock" and computerChoice == "scissors") or(playerChoice == "paper" and computerChoice == "rock")or\
        (playerChoice == "scissors" and computerChoice == "paper"):
              print(f"{playerChoice} beats {computerChoice}! You win")
              wins += 1
    else:
         print(f"{computerChoice} beats {playerChoice}! You lose!")
         losses += 1
    print(f"\nFinal Score - Wins: {wins}, Losses: {losses}, Ties:{ties}")
         
