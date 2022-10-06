a = input("Введите любое слово: ")
a = a.lower()
if list(reversed(a)) == list(a):
    print("----------------")
    print("Слово палиндром")
else:
    print("----------------")
    print("Слово не является палиндромом")