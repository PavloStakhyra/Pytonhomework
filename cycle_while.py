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
