n = int(input("Введите число: "))
result = []
for i in range(2, n+1):
    if i == 2 or i == 3:
        result.append(i)
    elif i % 2 == 0 or i % 3 == 0:
        continue
    else:
        result.append(i)

print(result)
print(len(result))
print(sum(result))