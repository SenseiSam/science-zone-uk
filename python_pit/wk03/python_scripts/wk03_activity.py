# Week 3: Week 3: Loops (For and While) - Class Activity

# Start with selecting a secret number and storing it as a variable
secret_number = 7

# We also need to create another variable called 'guess' to store the users guess
guess = 0

# To keep the program running forever until the secret number is guessed, a while loop is better to use than a for loop 
# Use a while loop to repeat all the code within the loop until the user guesses the secret number
# All the code inside the loop must be indented!
while guess != secret_number:
    
    # The input function collects data from the user and stores it in the variable 'guess'
    guess = int(input("Guess the number: "))

    # Use a conditional statement (if, elif, else) to see if the user has guessed the number or offer a hint
    # First is an if statement to check if guess is equal to the secret number
    # Use a break command to exit outside of the loop and continue the program
    if guess == secret_number:
        break

    # Next is an elif statement to check if the guess is bigger than the secret number
    elif guess > secret_number:
        print("Too High! The secret number is lower than your guess")

    # Finally an else statement as the number must be smaller than the secret number
    else:
        print("Too Low! The secret number is higher than your guess")

# Outside of the loop, this will be shown to the user once they guess the secret number
print("You guessed it! The secret number was " + str(secret_number))

    
