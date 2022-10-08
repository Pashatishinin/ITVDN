def first_function():
    print("Начало вызова")
    print(second_function(24, 45))
    print("Конец вызова")


def second_function(a, b):
    return a + b


first_function()
