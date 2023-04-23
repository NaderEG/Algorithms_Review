# Section 0.2 Fibonacci

def fib1(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib1(n - 1) + fib1(n - 2)

print(fib1(int(input())))