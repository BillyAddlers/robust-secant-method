def secant(x0, x1, err_tolerance, iter_limit, f):
	x0 = float(x0)
	x1 = float(x1)

	err_tolerance = float(err_tolerance)

	iter_limit = int(iter_limit)

	x2 = 0
	state = True
	current_iter = 1
	while state:
		if f(x0) == f(x1):
			print("ERRNOENT: Divide by zero!")
			break

		x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
		print(f"Iteration-{current_iter}, x2 = {x2} and f(x2) = {f(x2)}")
		x0 = x1
		x1 = x2
		current_iter = current_iter + 1

		if current_iter > iter_limit:
			print("ERR: Equation is not Convergent!")
			break

		state = abs(f(x2)) > err_tolerance

	print(f"\n Required root is: {x2}")
