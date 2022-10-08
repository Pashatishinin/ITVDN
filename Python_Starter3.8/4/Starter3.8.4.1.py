number = int(input("Enter number: "))
fib = [0, 1]
if number == 1:
    fib = [0]
elif number == 2:
    pass
else:
    while len(fib) < number:
        fib.append(fib[-1]+fib[-2])

print(fib)




