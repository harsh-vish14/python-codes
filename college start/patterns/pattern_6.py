def create(n):
    alphabets = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'
        , 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    # alphabets.reverse()
    result = n
    spaces = 0
    while True:
        print("\t"*spaces,end='')
        loopArray = list(reversed(range(result)))
        for i in loopArray:
            if(i == loopArray[0] or i == loopArray[-1]):
                print("\t1",end='')
            else:
                print(f"\t{alphabets[i-1]}",end='')
        print('')
        spaces += 1
        result -= 2
        if(result <= 0):
            break
create(7)

"""
output:

	1	E	D	C	B	A	1
		1	C	B	A	1
			1	A	1
				1
"""