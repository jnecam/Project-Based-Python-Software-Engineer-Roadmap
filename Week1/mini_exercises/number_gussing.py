trial = 3
secret = 7
guess = int(input("Guess a number between 1 and 10: "))
count = 0

while guess != secret and count < trial - 1:
    count += 1
    print(f"Wrong guess. You have {trial - count} trials left.")
    guess = int(input("Guess a number between 1 and 10: "))     
else:
    if guess == secret:
        print("You guessed the number!")
    else:
        print("Sorry, you've used all your trials. The secret number was 7.")

