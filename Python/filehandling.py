#!/bin/env python3

## use 'open' for opening files(manually)
##file_obj = open('cyberlab.txt', 'r')
##cyberlab_content = file_obj.read()
##print(cyberlab_content)
##file_obj.close()

## using with statement
##with open("cyberlab.txt", "r") as file:
    ##content = file.read()
    ##print(content)

## writing to a file
##with open("cyberlab.txt", "w") as file:
    ##file.write("Hello, Cyberlab!\n")
    ##file.write("This is a new line.\n")

##with open("cyberlab.txt", "r") as file:
    ##new_content = file.read()
    ##print(new_content)

## writing multiple lines
##lines = ["We are learning about python file handling"]
##print(lines)

## writing to a new file
with open("data.txt", "w") as file:
    for i in range (1, 10):
        file.write(f"{i}\n")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Open the file in append mode ('a') so new data is added, not overwritten
with open("data.txt", "a") as file:
    # Ask the user for input
    first_name = input("Enter your first name: ")
    class_name = input("Enter your class: ")
    year = input("Enter the year: ")

    # Write each input on a new line
    file.write(first_name + "\n")
    file.write(class_name + "\n")
    file.write(year + "\n")

print("Your details have been added to data.txt successfully!")


