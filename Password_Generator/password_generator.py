import string
import secrets


def contains_upper(password:str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True

    return False


def generate_password(lenght:int, symbols:bool, uppercase:bool):
    combination: str = string.ascii_lowercase + string.digits
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_lenght = len(combination)
    new_password:str = ''

    while True:
        #for _ in range(lenght):
        new_password += combination[secrets.randbelow(combination_lenght)]
        if contains_symbols(new_password) and contains_upper(new_password):
            return new_password


if __name__ == '__main__':
    for i in range(1, 6):
        new_password: str = generate_password(lenght=3, symbols=True, uppercase=True)

        specs: str = f'U: {contains_upper(new_password)}, S: {contains_symbols(new_password)}'
        print(f'{i}  -> {new_password} ({specs})')
