# What do these algorithms do?

def algorithm1(num1, num2):
  result = 0
  for loop in range(0, num1, 1):
    result += num2
  return result

def algorithm2(number):
  if number % 3 == 0:
    print("This number is valid!")
  else:
    print("This number is invalid!")

def algorithm3(num1, num2):
  # This one is a challenge. Don't panic if you don't get it!
  while num1 != num2:
    if num1 < num2:
      num2 -= num1
    else:
      num1 -= num2
  return num1
