#!/bin/env python3

# contact_book.py
import csv

FILENAME = "contacts.csv"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("Contact added!")

def view_contacts():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\nContacts:")
            for i, contact in enumerate(reader, start=1):
                print(f"{i}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
    except FileNotFoundError:
        print("No contacts found.")

def delete_contact():
    view_contacts()
    num = int(input("\nEnter contact number to delete: "))
    with open(FILENAME, "r") as file:
        contacts = list(csv.reader(file))
    if 1 <= num <= len(contacts):
        del contacts[num - 1]
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print("Contact deleted.")
    else:
        print("Invalid contact number!")

while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
