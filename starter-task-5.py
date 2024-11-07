# Set a secret number (you can change this value to anything)
secret_number = 7

# Ask the user to guess the secret number
guess = int(input("Guess the secret number: "))

# if the guess is correct
if guess == secret_number:
    print ("you are right")

# if the guess is too high
elif guess > secret_number:
  print ("the number is too high")
  print (input("guess again"))

# if the guess is too low
else:
   print ("the number is too low")
   print (input("guess again"))