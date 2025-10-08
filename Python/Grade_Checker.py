#!/bin/env python3

# Task: Grade Assignment Program
# This program asks the user for their score and assigns a letter grade.

print("=== Grade Assignment Program ===")

# Ask the user to enter their numeric grade
score = float(input("Enter your grade (0 - 100): "))

# Check and assign the letter grade using conditionals
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score! Please enter a value between 0 and 100."

# Display the result
print(f"Your grade is: {grade}")
