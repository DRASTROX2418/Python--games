#Author Saikumar.G


import random
secret = random.randint(1,10)

print("Guess the number Beta!")
guess = int(input("Choose a number from 1 to 10:"))

if guess == secret:
    print("Ganz richtig! You WON")

else:
    print("Nein ganz knap!, Hey Beta the number was:", secret)