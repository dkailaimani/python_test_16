# Task 1: Your Mood Today

# Problem Statement: Create a Python program using 
# a custom module that asks the user how they are feeling
# today and responds with a custom message based on the mood entered.

# Expected Outcome: The program should be able to take
# a user's mood as input (e.g., happy, sad, excited) 
# and return a corresponding custom message.
usersMood = input("ENTER MOOD: ")
def moodMessage(mood):
    response = {
        "nervous": "Brainstorm ways to relax. Maybe journal?",
        "relaxed": "Remain present.",
        "content": "Nice! Are you in this mood often?",
    }
    return response.get(mood.lower(), "Interesting! This mood won't last forever...")

print(moodMessage(usersMood))


# # Task 1: Contact List Manager

# # Problem Statement: Create a Python script using a custom 
# # module to manage a contact list. The script should allow adding,
# # removing, and displaying contacts stored in a list.

# # Expected Outcome: The program should accurately display the current 
# # month and year and successfully convert a user-input date string 
# # (e.g., "2023-03-15") into a datetime object, handling any invalid 
# # inputs gracefully.

contacts = []

def insertContact(name, phoneNum):
    contacts.append({'name': name, 'phoneNum': phoneNum})
    print(f"'{name}' WITH PHONE NUMBER'{phoneNum}' INSERTED!")

def deleteContact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"'{name}' DELETED!")
            return
    print(f"'{name}' DOES NOT EXIST.")

def viewContacts():
    if contacts:
        print("CONTACTS:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phoneNum']}")
    else:
        print("CONTACTS DON'T EXIST!")


# Task 1: Custom Module with Aliases

# Problem Statement: Create a custom module named text_utils.py
#  with functions for string manipulation (e.g., reversing a string, capitalizing). 
#  In your main script, import this module using an alias and utilize its functions.

# Expected Outcome: Your main script should be able to use the functions from text_utils.py via an alias, 
# demonstrating an understanding of custom module creation and aliasing.

import text_utils as tu

string = input("ENTER STRING: ")

reversedString = tu.reverseString(string)
capitalizedString = tu.capitalizeString(string)

print("STRING IN REVERSE:", reversedString)
print("CAPITALIZED STRING:", capitalizedString)



