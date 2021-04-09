data_list = ["Mason: 30", "Elo: 12", "Emily: 14", "Simon: 14"]



y_axis = []
def sep_names(data_list):
    name_list = []
    for data in data_list: 
        end_point = data.find(":")
        name = data[:end_point]
        name_list.append(name)
    return name_list

x_axis = sep_names(data_list)
print(x_axis)


def sep_ages(data_list):
    age_list = []
    for data in data_list:
        start_point = data.find(" ")
        age = int(data[start_point:]) + 1
        age_list.append(age)
    return(age_list)
y_axis = sep_ages(data_list)
print(y_axis)
