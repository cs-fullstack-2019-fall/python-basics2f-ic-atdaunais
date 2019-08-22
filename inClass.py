# imports the random module, sets the range for random selection between 1 and 100, then prints the number
import random
randomNum = random.randint(1, 100)
print(randomNum)

# asks for user input until q is entered. accounts for upper or lower case entry
userInput = ""
while userInput.upper() != "Q":
    userInput = input("Enter any input, or press 'q' to quit: ")

# sets the random number between 1 and 100
# takes a user guess and says whether they are too high, too low, or correct
rand_num = random.randint(1, 100)
userGuess = 0
while userGuess != rand_num:
    userGuess = int(input("Guess the correct number between 1 and 100: "))
    if userGuess > rand_num:
        print("Too high")
    elif userGuess < rand_num:
        print("Too low")
print(f"Correct! The secret number was {rand_num}")

# asks for a positive integer, then counts to the given number. quits if given 0 or a negative
userNum = 1
while userNum > 0:
    userNum = int(input("Please enter a positive integer: "))
    if userNum != 0:
        for x in range(0, userNum+1):
            print(x)
print("Goodbye")