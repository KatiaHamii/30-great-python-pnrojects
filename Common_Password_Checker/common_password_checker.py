def check_password(password:str):
    with open('passwords.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    if  len(password) == 0:
        print("Password cannot be empty. Please try again.")
    else:
        foundCommon = False
        for i, common_password in enumerate(common_passwords, start=1):
            if password == common_password:
                print(f'{password}: ❌(#{i})')
                foundCommon = True
        if not foundCommon:
            print(f'{password}: ✅ (Unique)')



def main():
    while True:
        user_password = input("Enter your password: ").strip()
        check_password(user_password)



if __name__ == "__main__":
    main()