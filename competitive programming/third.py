
n = int(input())
for x in range(0,n):
    matrix = int(input())
    arr = []
    col = []
    for i in range(matrix):
        col = []
        for j in range(matrix):
            n = input()
            col.append(n)
        arr.append(col)
    countincol = []
    rolinrow = []
    for x in range(matrix):
        countincol.append(arr[x].count("0"))
    for y in range(matrix):
        rolinrow.append(arr[0][y].count("0"))
    if (max(rolinrow) > max(countincol)):
        print(0)
    else:
        print(max(rolinrow)+1)


