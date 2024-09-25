# Week 2 Advanced Challenge: Conditional Logic with Multiple Inputs

# Instructions:
# 1. Modify the program to ask for both the user's age and favorite season.
# 2. Use both inputs to suggest a more personalized activity using if-elif-else statements.

# Start by greeting the user
print("Let's find a fun activity for you!")

# Ask for the user's age
age = int(input("How old are you? "))

# Ask for the user's favorite season
season = input("What is your favorite season? ").lower()

# Suggest an activity based on both age and season
if age < 13 and season == "summer":
    print("You should try building a sandcastle at the beach!")
elif age < 13 and season == "winter":
    print("How about having a snowball fight with your friends?")
elif 13 <= age < 18 and season == "summer":
    print("You could go surfing or play beach volleyball!")
elif 13 <= age < 18 and season == "winter":
    print("Snowboarding or ice skating might be fun!")
else:
    if season == "summer":
        print("Why not try taking a nature walk or going camping?")
    elif season == "winter":
        print("Maybe you can try cozying up with a good book or cooking something warm!")
    else:
        print("There are always new activities to try, no matter the season!")

# Final message
print("Hope you enjoy your personalized activity!")
