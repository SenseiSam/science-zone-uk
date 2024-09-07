userInput = input("Enter anything here: ")
print(userInput)

# user input will always be a string. You need to cast this to other data types if you want to use it.

integer = input("Enter a whole number: ")
integer = int(integer)
print(integer + 10)

# You'll  notice that if you enter something that isn't a whole number into the above code, it will crash. We will learn how to deal with this later.

name = input("What is your name? ")

string = input("What is your age? ")
age = int(string)

rating = int(input("Rate how you're feeling on a scale of 1-10: "))

print("Your name is " + name)
print("You are " + str(age) + " years old.")
print("You are feeling like a " + rating + " out of 10.")
