my_string = input("Enter a string: ")
new_str = ''
for i in range(0, len(my_string)):

    if i % 2 != 0:
        new_str += "_"
    else:
        new_str += my_string[i]
print(new_str)
