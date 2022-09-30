a = int(input("Введите число: "))
result = 1
for i in range(1, a+1):
    result *= i
print("_______________")
print(f"Факториалом числа {a} будет {result}")