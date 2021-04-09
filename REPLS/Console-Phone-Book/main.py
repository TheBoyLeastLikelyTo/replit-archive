import contacts
from os import system

main_message = """Simon's Phone Book

Phonebook Modes:

1: Add New Contact
2: Find Existing Contact
3: Delete Contact
4: Update Contact
"""

def userConfirm():
    input("Press enter to continue. ")

def prompt_add_contact():
    name = input("Please enter the contact's name: ")
    number = input("Please enter the contact's phone number: ")
    print(f"Adding {name} with {number}")
    contacts.add_contact(name, number)

def prompt_get_contact():
    name = input("Please enter the name to find: ")
    number = contacts.get_contact(name)

    if number:
        print(f"{name}'s number is {number}")
    else:
        print("Contact not found.")
    userConfirm()

def prompt_delete_contact():
    name = input("Please enter the name of the contact to delete: ")
    if contacts.delete_contact(name):
        print("Contact deleted")
    else:
        print("Contact not found")
    userConfirm()

def prompt_update_contact():
    name = input("Please enter the name of the contact to update: ")
    if not name in contacts.db:
        print("Contact not found.")
        return

    conta
    print("Contact updated")
    userConfirm()

def main():
    print(main_message)
    choice = input("Select Mode: ").strip() # !!
    if choice == "1":
        prompt_add_contact()
    elif choice == "2":
        prompt_get_contact()
    elif choice == "3":
        prompt_delete_contact()
    else:
        print("Invalid input.")

while True:
    system("clear")
    main()
