# Section 0.2 Fibonacci

def fib1(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib1(n - 1) + fib1(n - 2)

def fib2(n):
	if n == 0:
		return 0

	f = []

	f.append(0)
	f.append(1)

	for i in range(2, n+1):
		f.append(f[i-1] + f[i-2])
	return f[n]

print(fib2(int(input())))