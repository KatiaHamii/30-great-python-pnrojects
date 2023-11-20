import itertools
import string
import time

def common_guess(word:str) -> str | None:
    with open ('words.text', 'r') as words:
        word_list: list(str) = words.read().splitlines()

        for i, match in enumerate(word_list, start = 1):
            if match==word:
                return f'Common match: {match} (#{i})'

def brude_force(word:str, length:int, digits:bool=False, symbols:bool=False) -> str | None:
    chars: str = string.ascii_lowercase
    if digits:
        chars +=string.digits
    if symbols:
        chars += string.punctuation
    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts +=1
        guess:str = ''.join(guess)   #it returns a list of possible variations

        if guess == word:
            return f" {word} was ckacked in {attempts: ,} guesses"

        #print(guess, attempts)

def main():#
    print("Searching...")
    password: str = "1996"
    star_time:float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brude_force(password, length=4, digits=True, symbols=True):
            print(cracked)
        else:
            print("There was no match")

    end_time:float = time.perf_counter()
    print(round(end_time - star_time, 2), 's')


if __name__ == '__main__':
    main()
