# Guess My Birthday Game

from random import randint

name = input("Hi! What is your name? ")

# Guess 1

month = randint(1, 12)
year = randint(1924, 2019)

print("Guess 1:", name, "were you born in",
       month, "/", year, "?")

response = input("yes or no? ")

if response == "yes":
    print("I knew it!")
    exit()
else:
    print("Drat! Lemme try again!")

# Guess 2

month = randint(1, 12)
year = randint(1924, 2019)

print("Guess 2:", name, "were you born in",
       month, "/", year, "?")

response = input("yes or no? ")

if response == "yes":
    print("See, Second times the charm!")
    exit()
else:
    print("Grrr! I'll get it this time!")

# Guess 3

month = randint(1, 12)
year = randint(1924, 2019)

print("Guess 3:", name, "were you born in",
       month, "/", year, "?")

response = input("yes or no? ")

if response == "yes":
    print("See, Third times the charm!")
    exit()
else:
    print("I give up, you fooled me!")
