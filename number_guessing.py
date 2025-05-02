from random import randint


print("Welcome to the number guessing game.\nIm thinking of a number between 0 and 100.")


def game_on():
    level = input("Would you like to play easy or hard level?").lower()
    the_number = randint(0, 100)
    tries = 10
    while game_on:
        guess = int(input("Guess the number:"))
        if guess == the_number:
            print("Congrats, you guessed the number!")
            break
        elif guess < the_number:
            print("Too low.")
        elif guess > the_number:
            print("Too high.")
        tries -= 1
        if level == "hard" and tries == 5:
            print("You couldn't guess it in 5 tries.")
            break
        elif level == "easy" and tries == 0:
            print("You couldn't guess it in 10 tries.")
            break

        if level == "hard":
            print(f"Tries left {tries-5}")
        elif level == "easy":
            print(f"Tries left {tries}")

    play = input("Do you want to play again? y or n").lower()
    if play == "y":
        game_on()

game_on()


