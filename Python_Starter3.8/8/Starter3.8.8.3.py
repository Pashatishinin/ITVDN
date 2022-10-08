def divider(a, b):
    count = 1
    for i in range(1, b if b > a else a):
        if b % i == 0:
            if a % i == 0:
                count = i
    return count


print(divider(20, 50))
