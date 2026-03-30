

secret_number = 71
attempts = 3

for i in range(attempts):
    user_num = int(input("Enter a number: "))

    if user_num == secret_number:
        print("Congrats! You guessed it right.")
        break
    else:
        print("Wrong guess try again!")

    if i == attempts - 1:
        print("Sorry, come tomorrow.")