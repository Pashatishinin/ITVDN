import math

x = float(input("Введите значение х:"))
if -3.14 <= x and x <= 3.14:
    print(f"""x = {x}.
-3.14 <= x and x <= 3.14
________________________
y = {math.cos(x)} """)
elif x < -3.14:
    print(f"""x = {x}.
x < -3.14
_________
y = {x} """)
else:
    print(f"""x = {x}.
x > 3.14
________
y = {x} """)



