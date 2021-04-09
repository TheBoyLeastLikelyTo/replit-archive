import matplotlib.pyplot as plt

data_list = ["Mason: 30", "Elo: 12", "Emily: 14", "Simon: 14"]

def sep_names(data_list):
    name_list = []
    for data in data_list:
        end_point = data.find(":")
        name = data[:end_point]
        name_list.append(name)
    return name_list

def sep_ages(data_list):
    age_list = []
    for data in data_list:
        start_point = data.find(" ") + 1
        age = int(data[start_point:])
        age_list.append(age)
    return age_list
x_axis = sep_names(data_list)
print(x_axis)

y_axis = sep_ages(data_list)
print(y_axis)
#plt.bar(x_axis, y_axis)

#plt.savefig("example.png")
#find()
#index()
#split()
#slice()
#join() -