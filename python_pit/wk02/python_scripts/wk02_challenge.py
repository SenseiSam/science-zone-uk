# Week 2 Challenge: Conditional Statements

# Instructions:
# 1. Modify the program to ask for the user's favorite season (e.g., Summer, Winter, etc.).
# 2. Suggest an activity based on the season.
# 3. Use if, elif, and else to make decisions and respond to the user.

# Start by greeting the user
print("Let's find an activity based on your favorite season!")

# Ask for the user's favorite season
season = input("What is your favorite season? ")

# Suggest an activity based on the user's input
if season.lower() == "summer":
    print("Great! You should try going to the beach or having a barbecue.")
elif season.lower() == "winter":
    print("How about building a snowman or drinking hot chocolate?")
elif season.lower() == "spring":
    print("Spring is perfect for going on a nature hike!")
elif season.lower() == "autumn":
    print("Try visiting a pumpkin patch or enjoying a warm drink.")
else:
    print("I'm not sure about that season, but you can always try something new!")

# Final message
print("Enjoy your activity!")
