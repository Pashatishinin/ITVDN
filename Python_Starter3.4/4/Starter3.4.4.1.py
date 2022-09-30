a = 0
b = 0
while a == b or a > b:
    print("Второе значение должно быть больше первого")
    a = int(input("Введите первое значение: "))
    b = int(input("Введите второе значение: "))
    print("_______________")

for i in range(a, b + 1):
    print(i, end=" ")
