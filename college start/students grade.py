def gradeGiven(number):
    if (number >= 90):
        return 'A'
    elif (number < 90 and number >= 85):
        return 'B'
    elif (number < 85 and number >= 80):
        return 'C'
    elif (number < 80 and number >= 75):
        return 'D'
    else:
        return 'Fail'


print(gradeGiven(70))
