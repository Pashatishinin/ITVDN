A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
print(list(A-B))
print(list(A&B))
print(list(A.union(B)))

D = "a14b6fh"
if len(D) == len(set(D)):
    print("Все символы уникальны")
else:
    print("Не все символы уникальны")


