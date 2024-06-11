import random

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number")
    quit()

random_number = random.randint(1, top_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please guess a number")
        continue

    if user_guess == random_number:
        if guess == 1:
            print(f"You got it in {guess} guess!")
            break
        else:
            print(f"You got it in {guess} guesses!")
            break
    elif user_guess < random_number:
        print("The number is higher than your guess")
    else:
        print("The number is lower than your guess")