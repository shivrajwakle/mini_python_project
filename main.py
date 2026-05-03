import random

# 1 for snake
# -1 for water
# 0 for gun

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

youDict = {"s": 1, "w": -1, "g": 0}

if youstr not in youDict:
    print("Invalid input")
else:
    you = youDict[youstr]

    print("Computer chose:", computer)
    print("You chose:", you)

    # game logic (optimized)
    if computer == you:
        print("Draw!")

    elif (you - computer) == 1 or (you - computer) == -2:
        print("You win!")

    else:
        print("You lose!")