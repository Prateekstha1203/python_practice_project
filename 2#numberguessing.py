import random

#generating random numbers
#print(random.randint(1, 10))  # prints a random integer from 1 to 10 (inclusive)
# print(random.randrange(1, 10))  # prints a random integer from 1 to 9
# print(random.sample(range(1, 10), 3))  # prints a list of 3 unique random numbers from 1 to 9



# Get user input for the lower range
lowerRange = int(input("Enter the lower of the number range: "))
if lowerRange <= 0:
    print("Please enter a positive number for the lower range")
    quit()

topRange = int(input("Enter the top of the number range: "))
if topRange <= 0:
    print("Please enter a positive number for the lower range")
    quit()

# Ensure the top range is greater than the lower range
if lowerRange >= topRange:
    print("The lower range must be less than the top range")
    quit()
guesses = 0
randomNumber = random.randint(lowerRange, topRange)
while True:
    guesses += 1
    userGuess = int(input(f"Guess a number between {lowerRange} and {topRange}: "))
    if userGuess < lowerRange or userGuess > topRange:
        print("Please enter a number within the range")
        continue
    if userGuess == randomNumber:
        print("You guessed correctly!")
        break
    else:
        print("You guessed incorrectly")
        if(randomNumber>userGuess):
            print("The number is greater than your guess")
            continue
        else:
            print("The number is less than your guess")
            continue

print(f"You guessed the number in {guesses} guesses")
