# Week 1 Challenge: Python Basics
# Instructions:
# 1. Modify the program to ask the user three different questions (e.g., favorite hobby, favorite food, etc.).
# 2. Based on the user's input, respond with a personalized message for each question.
# 3. Ensure the program uses variables, input/output, and prints a final message summarizing the user’s responses.

# Start by greeting the user
print("Hello! Let's play a quick Q&A game.")

# Section 1: Ask for the user's favorite hobby
hobby = input("What is your favorite hobby? ")

# Section 2: Ask for the user's favorite food
food = input("What is your favorite food? ")

# Section 3: Ask for the user's favorite movie
movie = input("What is your favorite movie? ")

# Section 4: Respond to the user based on their answers
print("Wow, " + hobby + " sounds like a lot of fun!")
print("Yum, I love " + food + " too!")
print(movie + " is an awesome movie choice!")

# Section 5: Summarize the user's responses in a final message
print("So, you like " + hobby + ", enjoy eating " + food + ", and your favorite movie is " + movie + ". Thanks for sharing!")
