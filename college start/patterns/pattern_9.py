def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def create(n):
    counter = 0
    for i in range(1, n + 1):
        print('\t' * (n + 1 - i), end="")
        for j in range(i):
            print(f"\t{Fibonacci(counter)}\t", end="")
            counter += 1
        print("")


create(4)

"""
output:

					0	
				1		1	
			2		3		5	
		8		13		21		34	
"""
