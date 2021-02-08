name = ['raj', 'rahul', 'ramesh']
req = ['raj','rahul','harsh']
age = [21, 20, 22]


class Person:
    def __init__(self, name, age, req=''):
        self.name = name
        self.age = age
        self.req = req

    def print_data(self):
        if self.req == self.name:
            print(f"{str(self.name).capitalize()} is {self.age} year old")
        else:
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

