numbers = []
numbers.append(10)
numbers.append(12)
numbers.append(1)
numbers.append(31)
numbers.append(12)

print(numbers)
print(numbers[8])

total = 0
for loop in range(0, len(numbers), 1):
  total += numbers[loop]
print(total)
average = total / len(numbers)

print("The total is " + str(total))
print("The average is " + str(average))
