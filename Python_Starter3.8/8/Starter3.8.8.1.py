def number_security(num1, num2):
    if type(num1) != int or type(num2) != int:
        return 1
    elif num2 + num1 > 0:
        return 0
    elif num2 + num1 < 0:
        return -1


print(number_security(2, -4))
