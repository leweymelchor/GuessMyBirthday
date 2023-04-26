# Guess My Birthday Game

from random import randint

name = input("Hi! What is your name? ")

guess_number = 1
guess_word = {
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
}
for guess_number in range(1, 6):
    month = randint(1, 12)
    year = randint(1924, 2019)

    print("Guess", guess_number, ":", name, "were you born in",
        month, "/", year, "?")

    response = input("yes or no? ").lower()

    if response == "yes" and guess_number > 1:
        print("I knew it! See,", guess_word[guess_number], "times the charm!")
        exit()
    elif response == "yes":
        print("I knew it!")
        exit()
    elif guess_number == 3:
        print("Grrr! I'll get it this time!")
    elif guess_number == 5:
        print("I have better things to do. Smell-ya later")
        exit()
    else:
        print("Drat! Lemme try again!")
