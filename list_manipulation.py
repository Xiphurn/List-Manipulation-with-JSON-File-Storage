# Importing required libraries
import sys
import os 
import json

# Initializing variables
a = 1
liste = []
FILE_NAME = "list.JSON"
CUR_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(CUR_DIR, FILE_NAME)

# Creating and loading file if not exists
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file:
        json.dump(liste, file, indent = 4)
else :
    with open(FILE_PATH, "r") as file:
        liste = json.load(file)
            
# Main program loop
while True:
    while True:
        print("\n")
        choice = input("Choose from the following 5 options:\n \n1: Add an element to the list \n2: Remove an element from the list \n3: Display the list \n4: Clear the list \n5: Quit \n\nYour choice: ")
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Incorrect input!")
        else :
            break

    if choice == "1":
        element = input("Enter the name of the element to add: ")
        liste.append(element)
        print(f"The element \" {element} \" has been added to the list.")
    elif choice == "2":
        element = input("Enter the name of the element to remove: ")
        if element in liste:
            liste.remove(element)
            print(f"{element} has been removed from the list.")
        else:
            print(f"{element} is not in the list!")
    elif choice == "3":
        print("Here is the content of your list:")
        for i in liste:
            print(f"{a}: {i}")
            a += 1
        a = 1
    elif choice == "4":
        liste.clear()
        print("The list has been cleared.")
    elif choice == "5":
        print("Goodbye!")
        with open(FILE_PATH, "w") as file:
            json.dump(liste, file, indent = 4)
        sys.exit()

    print("\n")
    print("-" * 50)