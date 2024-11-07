# Set a secret number (you can change this value to anything)
secret_number = 7

# Ask the user to guess the secret number
guess = int(input("Guess the secret number: "))

# if the guess is correct
if guess == secret_number:
    # TODO: Print a message indicating the guess is correct

# if the guess is too high
elif guess > secret_number:
    # TODO: Print a message saying the guess is too high
    # TODO: Ask the user to guess again and update the guess variable

# if the guess is too low
else:
    # TODO: Print a message saying the guess is too low
    # TODO: Ask the user to guess again and update the guess variable

# TODO: Continue asking until the user guesses correctly (use a loop)
