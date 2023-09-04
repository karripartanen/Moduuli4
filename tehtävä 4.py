import random
guess = ""
randomint = random.randint(1,10)
while guess != randomint:
    guess = float(input("Guess a number between 1 and 10: "))
    if guess > randomint:
        print("Liian suuri arvaus")
    elif guess < randomint:
        print("Liian pieni arvaus")
    if guess == randomint:
        print("Oikein.")
