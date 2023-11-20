import random

def roll_dice (amount:int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls = []
    total = 0
    for i in range(amount):
        random_roll : int = random.randint(1, 6)
        rolls.append(random_roll)
    for j in range(len(rolls)):
        #print(rolls[j])
        total = total + rolls[j]

    return rolls, total

def main():
    while True:
        try:
            user_input = input("how many dice would you like to roll? ")
            if user_input.lower() == "exit":
                print("Thanks for playing")
                break
            rolls, total = roll_dice(int(user_input))
            print(*rolls, sep=', ')
            print(f'Total: {total}\n')
        except ValueError:
            print("please enter a valid number")

if __name__ == '__main__':
    main()



