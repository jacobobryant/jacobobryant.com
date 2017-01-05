import random

number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100, sucka")

guesses_left = 7
game_over = False

while not game_over:
    print("You have " + str(guesses_left) + " guesses left.")
    guess = int(input("Pick a number: "))
    guesses_left -= 1

    if guess == number:
        print("That is correct. You win.")
        game_over = True
    elif guess < number:
        print("Wrong! Your guess was too low.")
    else:
        print("Wrong! Your guess was too high.")

    if not game_over and guesses_left == 0:
        print("You're out of guesses. The number was " + str(number) + ". Moron.")
        game_over = True
