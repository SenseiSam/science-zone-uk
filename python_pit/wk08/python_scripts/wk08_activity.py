# Week 1: Introduction to Python - Class Activity

# Start with a simple print statement to greet the user
print("Hello! Let's get to know each other!")

# Ask the user for their name using the input function
# The input function collects data from the user and stores it in the variable 'name'
name = input("What is your name? ")

# Now that we have the user's name, we can personalize our responses
# Use the variable 'name' inside a print statement
print("Nice to meet you, " + name + "!")

# Ask the user for their favorite color
# Again, we use the input function and store the response in a variable called 'color'
color = input("What's your favorite color? ")

# Respond to the user's input
# We combine strings using '+' and include the 'color' variable in our response
print(color + " is a great color!")

# Let's ask for the user's age
# The input function returns data as a string, so we need to convert it to an integer using int()
age = int(input("How old are you? "))

# Now let's print a message based on their age
if age < 18:
    print("You're still young, " + name + "!")
else:
    print("You're an adult now, " + name + "!")

# Final message to end the conversation
print("It was fun chatting with you, " + name + ". Have a great day!")
