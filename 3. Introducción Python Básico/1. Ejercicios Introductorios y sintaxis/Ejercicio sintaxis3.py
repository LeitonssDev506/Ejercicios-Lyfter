

import random
secret_number = random.randint(1, 10)
while True:
    guess = int(input("Guess the secret number between 1 and 10: "))
    if guess == secret_number:
        print("That's right, you guessed the number.")
        break
    else:
        print(f"Try again! The secret number is not {guess}")