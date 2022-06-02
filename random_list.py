from random import randint

def random_list():
    s = [randint(a, b) for i in range(c)]
    print(s)

a = int(input("Start the list: "))
b = int(input("Finish the list: "))
c = int(input("Number of items: "))

random_list()