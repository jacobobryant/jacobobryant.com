import random

game_over = False
while not game_over:
    number = random.randint(1, 5)
    print("humledee bumbledee cow's pluck,")
    guess = int(input("how many fingers do I hold up? "))
    if guess != number:
        print(guess, "you said, but", number, "it was! So,")
    else:
        print(guess, "you said, and", number, "it was!")
        game_over = True
