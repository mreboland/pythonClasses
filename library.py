# The python standard library
# The Python standard library is a set of modules included with every Python
# installation. Now that we have a basic understanding of how functions and
# classes work, we can start to use modules like these that other programmers
# have written. We can use any function or class in the standard library
# by including a simple import statement at the top of our file. Let’s look
# at one module, random, which can be useful in modeling many real-world
# situations.

# ranint() is a function that takes two integer arguments and returns a randomly selected integer between (and including) those numbers
from random import randint, random
from random import choice

print(randint(1, 6))

# Another useful function is choice(). This function takes in a list or tuple and return a randomly chosen element
players = ['charles', 'martina', 'michael', 'florence', 'eli']
firstUp = choice(players)
print(firstUp)

# The random module shouldn't be used when building security-related apps. But it's good enough for many fun and interesting projects
# It is also possible to download modules from external sources which we'll learn about later on.

# 9-13. Dice: Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def rollDie(self):
        for rolls in range(10):
            print(randint(1, self.sides), "Roll:", rolls + 1)

print("\n6 sided die:")      
rollSix = Die()
rollSix.rollDie()

print("\n10 sided die:")
rollTen = Die(10)
rollTen.rollDie()

print("\n20 sided die:")
rollTwenty = Die(20)
rollTwenty.rollDie()  

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.

generator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
winningNumbers = []

for x in range(4):
    randomChoice = choice(generator)
    winningNumbers.append(randomChoice)

print("\nThe winning letters and numbers are:")
print(winningNumbers)
for winners in winningNumbers:
    print(f"\t{winners}")

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a message
# reporting how many times the loop had to run to give you a winning ticket.

generator = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
winningNumbers = []
myTicket = [1, 2, 3, 4]
draws = 0

# Creating infinite loop that'll only break once the winning numbers have been drawn
while True:
    # We need 4 letters and/or numbers for our lottery. This will repeat 4 times and append the 4 values to our list winningNumbers
    for x in range(4):
        # We use choice() to randomly draw from our list "generator". We save the random draw to "randomChoice" variable
        randomChoice = choice(generator)
        # We append the random choice to our list "winningNumbers"
        winningNumbers.append(randomChoice)
    # We have this print here to show output of the "winningNumbers" after 4 random choices have been added to it (more for debugging)
    print(winningNumbers)
    
    # If my ticket doesn't match the "winningNumbers" we need to continue with the loop
    if myTicket != winningNumbers:
        # We need to clear (empty) the list otherwise the infinite loop will keep appending numbers to the end of winningNumbers infinitely. We need to reset the list everytime to avoid that.
        winningNumbers.clear()
        # Counter to see how many tries it took
        draws += 1
        continue
    # If we won we do the below
    else:
        print(f"\nYou won! with {winningNumbers}")
        print(f"It took {draws} draws to win!")
        break

