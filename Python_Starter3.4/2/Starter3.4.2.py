a2 = input("Введите первое слово: ")
b2 = input("Введите второе слово: ")
print("------------")
print(a2, "," ,b2)
print()
a1 = int(input("Введите число a: "))
b1 = int(input("Введите число b: "))
x = int(input("Введите число x: "))
print("------------")
print(a1<x<b1)
print()
print("ax**2 + bx + c = 0")
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
print("------------")
result1 = b ** 2 - 4 * a * c
if result1<0:
    print("Нет Корней")
else:
    result2 = result1 ** 0.5
    result3 = b * (-1)
    x2 = (result3 - result2) / (2 * a)
    x1 = (result2 + result3) / (2 * a)

    print("x1 =",x1)
    print("x2 =",x2)

    print("Ответ1", a * (x1 ** 2) + b * x1 + c)
    print("Ответ1", a * (x2 ** 2) + b * x2 + c)


