#!/usr/bin/env python3

# Task 6: Login System Simulation
# Simulates a simple username-password login system.

users = {
    "admin": "1234",
    "user": "pass"
}

print("=== Login System ===")

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful! Welcome,", username)
else:
    print("Login failed! Invalid username or password.")
