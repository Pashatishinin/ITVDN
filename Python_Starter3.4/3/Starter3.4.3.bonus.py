import math

a = float(input("Введите первое значение: "))
operation = input("Введите одну из перечисленных операций( + , - , / , * , ** , sin , cos , tan ): ")
if operation == "sin":
    result = math.sin(a)
elif operation == "cos":
    result = math.cos(a)
elif operation == "tan":
    result = math.tan(a)
else:
    b = float(input("Введите второе значение: "))

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    elif operation == "**":
        result = a ** b
print("______________")
print(f"Ответ: {result}")