n = int(input("Enter the Numbers: "))
li = []
for i in range(n):
    li.append(int(input()))
# Bubble sort algorithm to sort the list

for i in range(n - 1):
    for j in range(0, n - 1 - i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print("The Sorted List is: ")
for i in li:
    print(i, end=" ")
