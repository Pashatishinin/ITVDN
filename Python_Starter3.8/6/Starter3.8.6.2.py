d = {"a": 3, "b": "hello", "c": 4, "d": -3}
new_d = {}
list = []
for i in d.values():
    if type(i) is int:
        list.append(i)

maximum = max(list)
for element in d:
    if d[element] == maximum:
        new_d[element] = d[element]
print(new_d)