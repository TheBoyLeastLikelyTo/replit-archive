import matplotlib.pyplot as plt

original_data = "Mason: 30-Liam: 12-Ivan: 9-Aditya: 10-Jonathan: 13-Aries: 25"

data_list = original_data.split("-")
print(data_list)

def grab_names(data_list):
    name_list = []
    for data in data_list:
        end_pos = data.find(":")
        name = data[:end_pos] 
        name_list.append(name)
    return(name_list)

def grab_ages(data_list):
    age_list = []
    for data in data_list:
        start_pos = data.find(" ") + 1
        age = data[start_pos:]
        age_intified = int(age)
        age_list.append(age_intified)
    return(age_list)


name_list = grab_names(data_list)
age_list = grab_ages(data_list)
print(name_list)
print(age_list)

plt.bar(name_list, age_list, color="red")
plt.title("My Graph")
plt.xlabel("Name")
plt.ylabel("Age")
plt.savefig("figure.png")
plt.show()