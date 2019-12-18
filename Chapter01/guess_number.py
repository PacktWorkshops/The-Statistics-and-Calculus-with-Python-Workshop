import random


# Generate a random true target.
true_value = random.randint(0, 10)

while True:
    guess = input('Enter your guess: ')

    # A try ... except block to handle potential invalid guesses (e.g., letters)
    try:
        guess = int(guess)
        if guess == true_value:
            print('Congratulations! You guessed correctly.')
            break
        elif guess > true_value:
            print('Lower.')
        else:
            print('Higher.')

    except ValueError:
        print('Please enter a valid number.')
