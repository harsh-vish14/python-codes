# This is Experiment 1

# a. Write a program to implement comments, datatypes, expressions, Input & Output functions

# datatypes
dataTypes = [12, 1.3, True, 'string', {'key': 'value'}]
print(type(dataTypes[0]))  # interger
print(type(dataTypes[1]))  # FLoat
print(type(dataTypes[2]))  # bool
print(type(dataTypes[3]))  # String
print(type(dataTypes[4]))  # dictionary

# expressions
num1 = 4
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 % num2)
print(num1 / num2)
print(num1 * num2)
print(num1 ** num2)
# logical expression
print(num1 == num2)
print(num1 != num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 < num2)
print(num1 > num2)
#  input
inputed = input('> ')
# output
print(inputed)



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
