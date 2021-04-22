
def createAPramide (n):
    alphabets = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'
        , 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    alphabets.reverse()

    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(1, i+2):
            newAlphabets = ''
            if(i%2 == 1):
                newAlphabets += (alphabets[-j])
                print(f'{newAlphabets[::-1]} ', end="")
            else:
                print("* ", end="")

        print("\r")

createAPramide(4)

"""
output:

   * 
  A B 
 * * * 
A B C D 
"""