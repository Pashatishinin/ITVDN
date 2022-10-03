def summa(num1, num2):
    return num1 + num2


def otnimanie(num1, num2):
    return num1 - num2


def umnozhenie(num1, num2):
    return num1 * num2


def delenie(num1, num2):
    if num1 == 0 or num2 == 0:
        print("_______________")
        print("На ноль делить нельзя!")
    else:
        return num1 / num2


def main():
    a = input("Пожалуйста напишите 'START' или 'STOP':")
    while a != "STOP":

        y = float(input("Введите первое значение: "))
        x = float(input("Введите второе значение: "))
        operation = input("Введите операцию ( + , - , * , / ): ")
        if operation == "+":
            result = summa(y, x)
        elif operation == "-":
            result = otnimanie(y, x)
        elif operation == "*":
            result = umnozhenie(y, x)
        elif operation == "/":
            result = delenie(y, x)
        print("_______________")
        print(result)
        a = input("Пожалуйста напишите 'START' или 'STOP':")
    print("Операция закончена")


main()
