import numpy as np
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
my_list_array_string = np.array(my_list, dtype="i")
print(my_list_array_string[1])
my_array = np.arange(9)
my_array_2 = np.arange(4,14,2)
print(my_array_2)
print(my_array)
#print(my_array[1])
sliced_array = my_array[:4]
#print(sliced_array)
#print(my_array.reshape(3,3))
print(type(my_list))
print(type(my_array))
print(my_array.dtype)
test_array = np.array([3, 4.5])
print(test_array)
print(np.linspace(2, 10, num=6))