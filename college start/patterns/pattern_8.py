def create(n):
    counter = 0
    for i in range(1,n+4):
        if(i%2 == 0):
            continue
        print(' '*(n+4-i),end="")
        nextLoop = list(range(i))
        for j in nextLoop:
            if(j == i-1 or j == 0):
                print(' *',end="")
            else:
                centerElement = nextLoop[round((i-1)/2)]
                if(centerElement == j):
                    print(' $', end="")
                else:
                    print(f' {counter}',end="")
        counter += 1
        print('')

create(4)

"""
output:

        *
      * $ *
    * 2 $ 2 *
  * 3 3 $ 3 3 *
"""