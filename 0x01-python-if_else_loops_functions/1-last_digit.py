#!/usr/bin/python3
import random
# Generate a random signed integer between -10000 and 10000 (inclusive)
number = random.randint(-10000, 10000)

# Extract the last digit (absolute value modulo 10)
last_digit = abs(number) % 10

# Print the message
print(f"Last digit of {number} is {last_digit}")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
