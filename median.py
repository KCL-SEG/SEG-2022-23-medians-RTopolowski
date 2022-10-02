"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

if len(numbers) % 2 == 0:
    # Even number of elements in "numbers"
    key = int(len(numbers) / 2)
    val1 = numbers[key]
    val2 = numbers[key - 1]
    print((val1 + val2) / 2)
else:
    # Odd number of elements in "numbers"
    key = int(math.floor(len(numbers) / 2))
    print(numbers[key])
