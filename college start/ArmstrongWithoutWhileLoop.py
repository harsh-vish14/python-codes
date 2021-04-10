# Python program to check if the number is an Armstrong number or not

# take input from the user
def IsArmstrong(num=0):
    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    for i in range(len(str(num))):
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # display the result
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


num = int(input("Enter a number: "))
IsArmstrong(num)

newNum = int(input("Enter a number: "))
IsArmstrong(newNum)
