from random import randint

lower_number, higher_number = 1, 10
random_number = randint(lower_number, higher_number)
trials = 3

print(f"Guess the number from {lower_number} to {higher_number}. You have only {trials} trials")

while True:
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError as e:
        print("Please enter a valid number")
        continue
    if user_guess > random_number:
        trials = trials - 1
        if trials == 0:
            print("You have no more trials")
            break
        print(f"The number is lower. You have {trials} trials")
    elif user_guess < random_number:
        trials = trials - 1
        if trials == 0:
            print("You have no more trials")
            break
        print("The number is higher. You have {trials} trials")
    else:
        print("Yes, you are right")
        break
