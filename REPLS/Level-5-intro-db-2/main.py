from replit import db
import random
import matplotlib.pyplot as plt

def main_screen():
    print("""if you want to enter data, type 1
    if you want to delete data, type 2
    if you want to delete all, type 3
    if you want to make a bar graph of all the data type 4
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
        print("sorry not a feature, please try again")
        main_screen()

# C in CRUD
def add_data():
    print("Please enter first name")
    name = input("type here:")
    print("Please enter your age")
    age = input("type here:")
    db[name] = age
    print(f"{name} who is {age} years old was added to the DB")
    main_screen()

# D in CRUD
def delete_data():
    print("Please enter in name to delete")
    key_to_delete = input("type here:")
    del db[key_to_delete]
    main_screen()

def delete_all():
    print("are you sure?")
    answer = input("type here:")
    if answer == "yes":
        keys_tuple = db.prefix("")
        for key in keys_tuple:
            del db[key]
    main_screen()

def create_fake_data():
    for i in range(10):
        random_number1 = random.randint(0, 100)
        random_number2 = random.randint(0, 100)
        random_number3 = random.randint(0, 100)
        fake_name = f"{random_number1}an{random_number2}"
        db[fake_name] = str(random_number3)

def create_bar():
    keys_tuple = db.prefix("")

    x_axis = grab_names(keys_tuple)
    y_axis = []
    plt.bar(x_axis, y_axis)
    plt.savefig("bar.png")

def grab_names(keys_tuple):
    names = []
    for key in keys_tuple:
        names.append(key)
    return(names)
    
# def grab_ages():

def main():
    main_screen()

main()