def hello_world():
    print("Hello, world!")

def concatenation():
    a = input("Введіть перше значення")
    b = input("Введіть друге значення")
    c = input("Введіть третє значення")
    print(a + b + c)

def if_elif():
    a = int(input("Введіть число A:"))
    b = int(input("Введіть число B:"))
    c = int(input("Введіть число C:"))
    if a > b:
        print("Сумне повідомлення.")
    elif b > a and b > c:
        print("Безмежно радісне повідомлення.")
    elif c >= b:
        print("Не дуже сумне повідомлення.")
    elif a == b:
        print("Рівенство - це круто!")

def cycle_while():
    a = int(input("Введіть число A:"))
    b = int(input("Введіть число B:"))
    c = int(input("Введіть число C:"))
    d = "Історія інкрементів:"

    while a < b:
        print("Поганий результат")
        a += c
        d += " " + str(a)
    print("Все добре, вітаю!")
    print(d)
hello_world()
concatenation()
if_elif()
cycle_while()