def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def priramidfibo (n):
    if n>0:
        fiboCounter = 0
        for x in range(0, n):
            for j in range(0, (n - x-1)):
                print("\t", end='')
            for j in range(0, n - (n - x-1)):
                print(f'{Fibonacci(fiboCounter)}\t', end='')
                fiboCounter+=1
            print('')
    else:
        print('invalid input')

priramidfibo(4)