
def createAPramide (n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print("",end=" ")
        k = k - 1
        for j in range(1, i+2):
                if((i+j)%2==0):
                    print(f'{1} ', end="")
                else:
                    print(f'{0} ', end="")
        print("\r")

createAPramide(4)