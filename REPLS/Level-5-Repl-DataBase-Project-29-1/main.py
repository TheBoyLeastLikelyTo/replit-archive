from replit import db
import matplotlib.pyplot as plt
#35.224.251.249:443
from os import system
def main_screen():
    print("""
    if you want to enter data, type 1
    if you want to delete data type 2
    if you want to delete all data type 3
    if you want to create a bar graph of data type 4
    
    """)
    
    choice = input("type here:")
    if choice == "1":
        add_data()
    elif choice == "2":
        delete_data()
    elif choice == "3":
        delete_all()
    elif choice == "4":
        create_bar()
    else:
        print("new features coming soon sorry")
        system("clear")
        

# C in CRUD
def add_data():
    print("Please enter your first name.")
    name = input("type here:")
    print("Please enter your age")
    age = input("type here:")
    db[name] = age
    main_screen()
# D in CRUD
def delete_data():
    print("what key do you want to delete?")
    key_to_delete = input("type here:")
    del db[key_to_delete]
    main_screen()

def delete_all():
    print("Enter the password")
    answer = input("type here:")
    if answer == "yes":
        keys_tuple = db.prefix("")
        for key in keys_tuple:
            del db[key]

    main_screen()

# R in Crud
def create_bar():
    keys_tuple = db.prefix("")
    x_axis = grab_names(keys_tuple)
    y_axis = grab_ages(keys_tuple)
    plt.bar(x_axis, y_axis)
    plt.savefig("bardata.png")
    
def grab_names(keys_tuple):
    name_list = []
    for key in keys_tuple:
        name = key
        name_list.append(name)
    return(name_list)

def grab_ages(keys_tuple):
    age_list = []
    for key in keys_tuple:
        age = int(db[key])
        age_list.append(age)
    return(age_list)
    
def main():
    main_screen()
main()
