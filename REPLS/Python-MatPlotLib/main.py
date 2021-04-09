my_string1 = "1: masons bassett"
my_string2 = "10000000: simon field"

def test(test_string):
	start_loc = test_string.index(" ") + 1
	print(test_string[start_loc:])

test(my_string2)