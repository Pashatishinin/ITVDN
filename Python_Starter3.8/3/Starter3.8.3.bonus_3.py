number = int(input("Enter your number: "))
if number < 0:
    if abs(number) // 1000 >= 1:
        print(f"Number {number} below 0 and count more then 3")
    elif abs(number) // 100 >= 1:
        print(f"Number {number} below 0 and count 3")
    elif abs(number) // 10 >= 1:
        print(f"Number {number} below 0 and count 2")
    else:
        print(f"Number {number} below 0 and count 1")
elif number > 0:
    if number // 1000 >= 1:
        print(f"Number {number} above 0 and count more then 3")
    elif number // 100 >= 1:
        print(f"Number {number} above 0 and count 3")
    elif number // 10 >= 1:
        print(f"Number {number} above 0 and count 2")
    else:
        print(f"Number {number} above 0 and count 1")
else:
    print(f"Number {number} is 0")
