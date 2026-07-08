#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:29:59 2026

@author: alissadinsmore
"""

# Global variable used to track the total number of dogs added to the system
dog_count = 0


def addDog(dog_list):
    """Asks the user for dog details and appends them to the list."""
    global dog_count
    
    print("\n--- Add a Dog ---")
    # Prompt user for input data regarding the dog's attributes
    name = input("Dog Name: ")
    breed = input("Dog Breed: ")
    age = input("Age: ")
    weight = input("Weight: ")
    
    # Organize the collected user data into a clean dictionary structure
    dog = {
        'name': name,
        'breed': breed,
        'age': age,
        'weight': weight
    }
    
    # Append the new dog dictionary into our main list structure
    dog_list.append(dog)
    
    # Increment the global counter to keep track of total dogs
    dog_count += 1
    print(f"{name} has been added successfully!")


def viewDogs(dog_list):
    """Iterates through the list and displays all rescue dogs."""
    print("\nRescue Dogs")
    print("Dog\t | Breed\t | Age\t | Weight")
    print("-" * 50)
    
    # Iterate through every dog item inside the data list
    for dog in dog_list:
        # Format and display each dog's details line by line
        print(f"{dog['name']}\t | {dog['breed']}\t | {dog['age']}\t | {dog['weight']}")


def findDog(dog_list):
    """Searches for a dog by name in the list."""
    print("\n--- Find Dog ---")
    search_name = input("Enter dog name to search: ")
    
    # Control flag variable to monitor if a search match is discovered
    found = False
    
    # Loop through the table to check each dog's name against the search query
    for dog in dog_list:
        # If the dog name matches (case-insensitive)
        if dog['name'].lower() == search_name.lower():
            print(f"Found {dog['name']}")
            found = True  # Switch flag to True since we found a match
            break         # Terminate the loop early to optimize execution
            
    # If the entire loop finished and no dog was found
    if not found:
        print(f"Sorry, unable to find {search_name}")


def menu(dog_list):
    """Displays the menu loop and handles user selections."""
    # Infinite loop to keep the user inside the application menu
    while True:
        print("\nDog Rescue")
        print("1. Add a Dog")
        print("2. View Dogs")
        print("3. Find Dog")
        print("4. Quit")
        
        choice = input("Select a choice: ")
        
        # Choice 1: User chose to add a brand new dog record
        if choice == '1':
            addDog(dog_list)
            
        # Choice 2: User chose to display all dog data
        elif choice == '2':
            viewDogs(dog_list)
            
        # Choice 3: User chose to search for a specific dog name
        elif choice == '3':
            findDog(dog_list)
            
        # Choice 4: User chose to exit out of the script safely
        elif choice == '4':
            print("Goodbye")
            break  # Break out of the menu loop to end execution
            
        # Choice Else: Triggered if user types anything outside of options 1-4
        else:
            print("Invalid choice, please select 1, 2, 3, or 4.")


def main():
    """Initializes the main dog table (list) and starts the menu."""
    # Setup the table structure using an empty Python list
    rescue_dogs = []
    
    # Call the operational menu and pass the table reference down
    menu(rescue_dogs)

# Standard Python safety mechanism to trigger main() when executed as a script
if __name__ == "__main__":
    main()