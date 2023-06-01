import random

dice1 = random.randrange(1,6)
dice2 = random.randrange(1,6)
dice3 = random.randrange(1,6)

total = dice1 + dice2 + dice3

if total > 9:
    print("Big")
elif total < 9:
    print("Small")

print(f"The total is {total}")
