# Byte Array

str = "Welcome to Python Programming"

# encoding the string with unicode 8 and 16

array1 = bytearray(str, 'utf-8')
array2 = bytearray(str, 'utf-16')

print(array1)
print(array2)

# size of array
size = 3

# will create an array of given size
# and initialize with null bytes
array1 = bytearray(size)

print(array1)

# simple list of integers
list = [1, 2, 3, 4]

# iterable as source
array = bytearray(list)

print(array)
print("Count of bytes:", len(array))

print("\n")

# Range Function

# printing a number
for i in range(10):
    print(i, end=" ")
print()

# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")
print()

# performing sum of natural
# number
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum of first 10 natural number :", sum)

# Printing odd natural numbers till 11

for i in range(1, 11, 2):
    print(i, end=" ")

print("\n")

# Sets

set1 = {1, 2, 3, 2, 1, 4}
print(set1)  # doesnt allows duplicates

set2 = set([1, 2, 3, 2])
print(set2)  # list to set typecasting

a = set()
print(type(a))

set1.add(5)  # adding a element in set
print(set1)

set1.update([7, 8, 9])  # adding multiple elements in set
print(set1)

set1.discard(4)  # remove element if it is present otherwise continue the further execution
print(set1)

set1.discard(2)  # remove element if it is present otherwise throws error
print(set1)

print(set1.pop())  # pops random element from set

set2.clear()  # to clear all elements from the set
print(set2)

# Set operations

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)  # Union
print(A & B)  # Intersection
print(A - B)  # Set Difference
print(A ^ B)  # Symmetric Difference

# Set Membership

set3 = set("apple")

# check if 'a' is present
print('a' in set3)

# check if 'p' is present
print('p' not in set3)
