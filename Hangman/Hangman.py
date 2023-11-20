from random import choice


def run_game():
    word = choice(["apple", "secret", "banana"])

    username = input("What is your name?  ")
    print(f"Welcome to the game, {username}")

    guessed = ""
    tries = 3
    while tries > 0:
        blanks = 0

        print("Word: ", end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1
        print()

        if blanks == 0 or guessed == word:
            print("You've got it")
            break

        guess = input("Enter a letter: ")
        if len(guess) > 1:
            print("You have to enter only ONE letter")
            continue
        if guess in guessed:
            print(f'You have alredy used: "{guess}". Try another one)')
            continue

        guessed += guess
        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong. You have {tries} tries")

            if tries == 0:
                print("You lost")
                break


if __name__ == '__main__':
    run_game()
