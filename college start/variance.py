# Variance of List
test_list = [6, 7, 3, 9, 10, 15]
print("The original list is : " + str(test_list))
mean = sum(test_list) / len(test_list)
res = sum((i - mean) ** 2 for i in test_list) / len(test_list)
print("The variance of list is : " + str(res))
