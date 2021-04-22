def create(n):
    alphabets = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'
        , 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    charCount = 0
    numberCount = 1
    entered = False
    for i in range(1,n+1):
        for j in range(i):
            if (entered):
                if(alphabets[charCount]=="C"):
                    charCount += 1
                print(f'{alphabets[charCount]} ', end="")
                charCount += 1
                numberCount += 4
                entered = False
            else:
                entered = True
                print(f'{numberCount} ', end="")
        print("")


create(4)

"""
output:

1 
A 5 
B 9 D 
13 E 17 F 
"""