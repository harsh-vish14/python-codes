#
# def computeXOR(n):
#
#     if n % 4 == 0:
#         return n
#     if n % 4 == 1:
#         return 1
#     if n % 4 == 2:
#         return n + 1
#     return 0
#
#
# print(computeXOR(1000))


def checkXOR(views):
    if (max(views) > 65):
        print(0)
    else:
        print(65)

n = int(input())
for x in range(0,n):
    views = []
    videos = int(input())
    for y in range(0,videos):
        v = int(input())
        views.append(v)
    checkXOR(views)
