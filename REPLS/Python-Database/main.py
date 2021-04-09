from replit import db
import random
import matplotlib.pyplot as plt

def main_screen():
    print("""
    if you want to enter data, type 1
    if you want to delete data, type 2
    if you want to delete all, type 3
    if you want to make a bar graph of all the data type 4
    """)
    choice = input("type here:").strip()
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
    name = input("type here:").lower().strip()
    if name.isalpha():
      print("Please enter your age")
      age = input("type here:").strip()
      if age.isnumeric():
        db[name] = int(age)
        print(f"{name} who is {age} years old was added to the DB")
      else:
        print("wrong input try again please")
    else:
      print("not a valid name")
    main_screen()

# D in CRUD
def delete_data():
    print("Please enter in name to delete")
    database_keys = db.prefix("")
    key_to_delete = input("type here:").lower().strip()
    if key_to_delete in database_keys:
        del db[key_to_delete]
        print("success key deleted")
    else:
      print("this name does not exist")
    main_screen()

def delete_all():
    print("are you sure?")
    answer = input("type here:").lower().strip()
    if answer == "yes":
      keys_tuple = db.prefix("")
      for key in keys_tuple:
          del db[key]
      print("all keys have been destroyed")
    else:
      print("deletion was canceled")
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
  ages = []

  for name in keys_tuple:
    age = db[name]
    ages.append(age)

  plt.bar(x_axis, ages)
  plt.savefig("bar.png")
  print("bar graph successfully exported to files")
  main_screen()
def grab_names(keys_tuple):
  names = []
  for key in keys_tuple:
    names.append(key)
  return(names)
    
# def grab_ages():

def main():
    main_screen()

main()

"""    keys_tuple = db.prefix("")

    x_axis = grab_names(keys_tuple)
    y_axis = []
    plt.bar(x_axis, y_axis)
    plt.savefig("bar.png")"""