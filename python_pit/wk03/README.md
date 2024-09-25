
# Week 3: Loops (For and While)

## Objectives:
- Understand how loops allow you to repeat blocks of code.
- Learn how to use `for` and `while` loops to iterate through data.

## Key Concepts:
1. **For Loop**: Repeats a block of code a set number of times, often used to iterate over a sequence (like a list or a range of numbers).
   ```python
   for i in range(5):
       print(i)
   ```
2. **While Loop**: Repeats a block of code while a certain condition is true.
   ```python
   while guess != secret_number:
       guess = int(input("Guess the number: "))
   ```
3. **Break and Continue**: Special commands to control loops:
   - `break`: Exits the loop completely.
   - `continue`: Skips to the next iteration of the loop.

## Tasks:
1. Write a number guessing game where the user tries to guess a number between 1 and 10, and the program gives hints.
2. Create a program that prints out multiplication tables based on user input.
