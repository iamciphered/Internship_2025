#!/bin/env python3

# Task 2: Basic Calculator
# Performs addition, subtraction, multiplication, or division based on user input

print("==== Basic Calculator ====")
print("Choose operation: +, -, *, /")

num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator.")
