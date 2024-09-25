# Week 2: Conditional Statements and Logic - Class Activity

# Instructions:
# 1. This program asks for the user's age and suggests an activity based on their response.
# 2. Use conditional statements (if, elif, else) to make decisions.

# Start by greeting the user
print("Welcome to the activity suggestion program!")

# Ask for the user's age
age = int(input("How old are you? "))

# Use conditional statements to suggest an activity based on the user's age
if age < 13:
    print("You should try playing on the swings at the park!")
elif 13 <= age < 18:
    print("How about learning a new sport, like basketball or skateboarding?")
else:
    print("Maybe you can start a new hobby like painting or photography!")

# Final message
print("Hope you enjoy your activity!")
