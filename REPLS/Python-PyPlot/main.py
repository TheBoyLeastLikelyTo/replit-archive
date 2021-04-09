import matplotlib.pyplot as plt
x_axis = ["mon", "tues", "wed", "thurs", "fri"]
data_list = [1, 2, 3, 4, 5]
data_list1 = [3, 4, 2, 1, 7]
plt.plot(x_axis, data_list)
plt.plot(x_axis, data_list1)
plt.savefig("example.png")