from secant import secant

input_x0 = input("Insert x0: ")
input_x1 = input("Insert x1: ")

err_tolerance = 0.0000001
iter_limit = 25


def f_case1(x):
	return x ** 3 - x ** 2 - x + 1


def f_case2(x):
	return 5 * x ** 2 - 3 * x - 14


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	# First case
	secant(input_x0, input_x1, err_tolerance, iter_limit, f_case1)
	# Second case
	secant(input_x0, input_x1, err_tolerance, iter_limit, f_case2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
