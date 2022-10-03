def operation(num1, num2, num3):
    return ((num1 + num2 + num3) / 3)


def name():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    print("_______________")
    print("Среднее значение: ", operation(a, b, c))

name()


