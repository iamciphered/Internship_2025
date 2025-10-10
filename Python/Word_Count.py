# word_count.py
# Counts the number of words in file
def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            lines = text.splitlines()
            words = text.split()
            print(f"\nLines: {len(lines)}")
            print(f"Words: {len(words)}")
            print(f"Characters: {len(text)}")
    except FileNotFoundError:
        print("File not found.")

def add_text(filename):
    new_text = input("Enter text to add: ")
    with open(filename, "a") as file:
        file.write(new_text + "\n")
    print("Text added successfully!")

filename = "textfile.txt"

while True:
    print("\n=== WORD COUNT PROGRAM ===")
    print("1. View Word Count\n2. Add New Text\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        count_words(filename)
    elif choice == "2":
        add_text(filename)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
