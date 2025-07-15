import random

comp = random.randint(0, 3)

winner = ""

user = int(input("Enter your choice (0 for stone, 1 for paper, 2 for scissors): "))

if comp == user:
    winner = "It's a tie Match!"
elif (
    (comp == 0 and user == 2) or (comp == 1 and user == 0) or (comp == 2 and user == 1)
):
    winner = "Computer wins!"
else:
    winner = "You win!"

print(winner)
