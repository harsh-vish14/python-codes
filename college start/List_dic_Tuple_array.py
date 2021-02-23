# Write python programs to understand List, Tuple, Dictionary and Arrays

# List examples:
# Create list of from 0 to 20 and remove odd element from the list
def checkEven(number):
    if (number % 2 == 0):
        return True
    else:
        return False


numbers = list(range(0, 21))
print(numbers)
# this will remove all odd number from the list

for number in numbers:
    if not checkEven(number):
        numbers.remove(number)

# this numbers will have only odd numbers
print(numbers)
# adding the last element in the list
numbers.append("Using append function to append a string in number list")
print(numbers)
# removing the last element from the list
numbers.pop()
print(numbers)
# reversing the list
numbers.reverse()
print(numbers)
# counting the number count in the list
print(numbers.count(2))
# inserting the element at particular index
numbers.insert(3, 'Inserting the string at index 3')
print(numbers)
# getting the index of element 10
print(numbers.index(10))
# add the new list at end of the numbers list using extent function
newList = [11, 22, 33, 44, 55, 66, 77, 88]
numbers.extend(newList)
print(numbers)
# sorting the unSortedList using sort function
unSortedList = [1, 4, 24, 6, 7, 1, 0, 3, 2, 5]
unSortedList.sort()
print(unSortedList)
# removing all elements from the list
numbers.clear()
print(numbers)

# Tuple examples
# tuple is immutable so we have to make
tupleList = (1, 2, 3, 4, 5, 4, 4, 5, 6)
# we can add delete or update the tuple
# we can do only some functions
# this function is give the index of 3
print(f"this is tuple index of 3 : {tupleList.index(3)}")
print(f"this is count of 4 in tuple list: {tupleList.count(4)}")
# we can also create tuple from the list
myList = [23, 4, 5, 2, 23, 3]
print(type(myList))
convertingToTuple = tuple(myList)
print(f'coverted to tuple type: {type(convertingToTuple)} and data in the : {convertingToTuple}')
# we can also create tuple by this way also
Username = 'FirstName MiddleName LastName'
email = 'xyz123@gmail.com'
password = 'ASimplePassword'
# adding this to tuple
userDetails = (Username, email, password)
print(userDetails)

# Example of Dictionary
# below is creating the Dictionary
dicMeaning = {
    'API': 'API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.',
    'python': 'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.',
    'Java': 'Java is a high-level programming language developed by Sun Microsystems. It was originally designed for developing programs for set-top boxes and handheld devices, but later became a popular choice for creating web applications.'
}
# printing the hole Dictionary
print(dicMeaning)
# printing values using keys name
print(dicMeaning['API'])
# adding new data in Dictionary
dicMeaning['newData'] = 'adding new data in Dictionary python'
print(dicMeaning['newData'])
# we can also print a key with values
for key in dicMeaning:
    print(f'Key: {key}')
    print(f'Value: {dicMeaning[key]}')

# Array examples:
import array as arr
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
# changing first element
numbers[0] = 0
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])
# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])