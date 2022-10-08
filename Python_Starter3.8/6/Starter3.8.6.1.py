d = {"a": 3, "b": 0, "c": 4, "d": -3}
new_d = {}
list = d.values()
maximum = max(list)
for element in d:
    if d[element] == maximum:
        new_d[element] = d[element]
print(new_d)
print(maximum)


