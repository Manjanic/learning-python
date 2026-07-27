import random
best_score = None
while True:
    print("Welcome to Number guessing Game")
    print("1. Easy (1- 50)")
    print("1. Hard (1- 100)")
    choice = int(input("Pick 1 or 2: "))
    if choice == 1:
        secret= random.randint(1,50)
        max_num =50
    elif choice == 2:
        secret = random.randint(1, 100)
        max_num = 100
    else:
        print("Invalid choice")
        continue
    attempts=0
    while True:
        try:
          guess = int(input(f"Guess number between 1 and {max_num}: "))
        except ValueError:
            print("Please type real number")
            continue
        attempts+=1
        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"correct you go it in {attempts} guess(es)")
            if best_score is None or attempts < best_score:
                best_score = attempts
                print("New best score !")
            play_again = input("Play again (y/n): ").lower()
            if play_again != "y":
                print("Thanks for playing! ")
                break
        
    


 