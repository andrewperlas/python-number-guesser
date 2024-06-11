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

print(f"The number you typed was {top_range}")

random_number = random.randint(0, top_range)