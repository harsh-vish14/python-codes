# This is Experiment 1

# a. Write a program to implement comments, datatypes, expressions, Input & Output functions

dataTypes = [12, 1.3, True, 'string', {'key': 'value'}]
# VariableName = [Integer , Float, bool, string, dictionary]
for data in dataTypes:
    print(type(data))


# b. WAP to find the GCD and LCM of any two numbers

# this is function will be used for computing lcm
def lcm(a, b):
    return a * b / gcd(a, b)


# this function will help to compute GCD
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
print("The L.C.M. is", lcm(num1, num2))
print("The G.C.D. is", gcd(num1, num2))
