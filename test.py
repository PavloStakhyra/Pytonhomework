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