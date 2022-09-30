a = int(input("Введите высоту прямоугольника: "))
for i in range(a):
    for j in range(i+1):
        print("*", end="  ")
    print()
