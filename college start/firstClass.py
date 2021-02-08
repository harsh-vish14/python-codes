name = ['raj', 'rahul', 'ramesh']
req = ['raj','rahul','harsh']
age = [21, 20, 22]


class Person:
    def __init__(self, name, age, req=''):
        self.name = name
        self.age = age
        self.req = req

    def print_data(self):
            print(f"{str(self.name)} is {self.age} year old")
    def do_capi(self,name):
        self.name = str(self.name).capitalize()

list_obj = []
for i in range(len(name)):
    obj = Person(name[i], age[i])
    list_obj.append(obj)

for i in list_obj:
    if i.name in req:
        i.do_capi(i.name)
    i.print_data()


def fizzbuzz(number):
    output = ''
    if (number % 3 == 0):
        output += 'fizz'
    if (number % 5 == 0):
        output += 'buzz'
    if (output == ''):
        return number
    return output


# for i in range(1, 101):
#     print(fizzbuzz(i))

def counter(s1):
    count_data = unique(s1)
    output = []
    count = 1
    for i in range(len(s1) - 1):
        if (s1[i] == s1[i + 1]):
            count += 1
        else:
            output.append(count)
            count = 1
    output.append(count)
    count = ''
    for i in range(len(count_data)):
        count += "" + str(count_data[i]) + str(output[i])
    return count


def unique(list1):
    list1 = list1 + ' '
    uniqe_list = []
    for i in range(len(list1) - 1):
        if (list1[i] != list1[i + 1]):
            uniqe_list.append(list1[i])
    return uniqe_list


print(counter('aabbbca'))


def reverse(l1):
    for i in range(len(l1) // 2):
        l1[i], l1[len(l1) - i - 1] = l1[len(l1) - i - 1], l1[i]
    return l1


print(reverse([1, 2, 3, 4, 5]))


matric = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def digonal(matric):
    digonal_array = []
    reverse_digonal_array = []
    for i in range(len(matric)):
        digonal_array.append(matric[i][i])
    for i in range(len(matric)):
        reverse_digonal_array.append(matric[i][len(matric)-i-1])
    print(digonal_array)
    print(reverse_digonal_array)

# digonal(matric)

l1 = [[1, 2, 3],
      [14, 19, 13],
      [7, 8, 19]]


def get_ver(i):
    temp = []
    for j in range(len(l1)):
        temp.append(l1[j][i])
    return max(temp)


for i in range(len(l1)):
    m1 = min(l1[i])
    if m1 == get_ver(l1[i].index(m1)):
        print(m1)

