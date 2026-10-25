#Author Saikumar.G


import random
secret = random.randint(1,20)

print("Guess the number Beta!")
guess = int(input("Choose a number from 1 to 20:"))

if guess == secret:
    print("Ganz richtig! You WON")

else:
    print("Nein ganz knap!, Hey Beta the number was:", secret)
