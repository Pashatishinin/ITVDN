def function(n):
    if n == 0:
        return 0
    else:
        return n + function(n-1)

print(function(int((input("Введите любое число: ")))))