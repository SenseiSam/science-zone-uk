# Week 1 Advanced Challenge: Python Basics with Decision Making
# Instructions:
# 1. Modify the program to ask the user five different questions (e.g., name, favorite hobby, favorite food, favorite color, favorite number).
# 2. Based on the user's input, provide unique responses.
# 3. Add decision-making using conditional statements (`if` statements) to customize the responses. 
# 4. Use at least one comparison for a numerical value (e.g., favorite number) to change the response.

# Start by greeting the user
print("Welcome to the advanced Q&A game!")

# Section 1: Ask for the user's name
name = input("What's your name? ")

# Section 2: Ask for the user's favorite hobby
hobby = input("What is your favorite hobby, " + name + "? ")

# Section 3: Ask for the user's favorite food
food = input("Yum! What is your favorite food? ")

# Section 4: Ask for the user's favorite color
color = input("What is your favorite color? ")

# Section 5: Ask for the user's favorite number (using int() to convert the input to a number)
number = int(input("Lastly, what's your favorite number? "))

# Section 6: Respond to the user based on their answers
print("Cool! " + hobby + " is a great way to spend your time.")
print("I could go for some " + food + " right now!")

# Section 7: Use conditionals to customize the response based on the favorite number
if number > 10:
    print("Wow, " + str(number) + " is a big number!")
elif number < 5:
    print(str(number) + " is a small number, but it's still great!")
else:
    print(str(number) + " is a perfect number!")

# Section 8: Respond to the favorite color and wrap up the program
print("Finally, " + color + " is such a vibrant color. Thanks for sharing all these cool things about yourself, " + name + "!")
