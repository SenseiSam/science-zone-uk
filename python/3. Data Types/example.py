'''
Python has different ways of storing data, known as data types. This is so the computer understands what the data means and what can be done with it.

Some of the common data types are:
- Whole numbers which are called integers in Python.
- Decimals/Fractions which are known as floats or reals.
- True/False statements are known as Booleans
- Strings of characters, or text. e.g 'bike', '42hudfh9' (we usually just call these strings)

Here is a brief demo showcasing the assignment of the 4 data types listed above into a variable
'''

# integer
num1 = 12
answerToEverything = 42

# float
num2 = 13.34
pi = 3.141592653589

# boolean
state1 = True
state2 = False

# string
fruit = "apple"
dessert = 'cake'

'''
Notice that two different types of quotes were used when assigning these string variables. These both do the same thing in Python.
The string is the only data type that requires quotes when assigning it.

If you are not sure of a data type you can always use the type() function. Pass this into a print() to see the variable's data type your answer
'''

num1 = 12
datatype = type(num1)
print(datatype)

string = "Hello world!"
print(type(string))

# Challenge: what data type will num3 below be?
num1 = 4
num2 = 7
num3 = num1 + num2

# Extend: What data type will num3 be if num1 or num2 were floats?




