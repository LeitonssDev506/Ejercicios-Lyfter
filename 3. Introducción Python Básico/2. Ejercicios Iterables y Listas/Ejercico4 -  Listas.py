my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = []

for i in my_list:
    if i % 2 == 0:  # Si el número es par
        new_list.append(i)

my_list = new_list
print(my_list)