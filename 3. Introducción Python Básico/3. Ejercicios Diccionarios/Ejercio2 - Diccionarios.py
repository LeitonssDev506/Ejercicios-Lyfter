

list_a = ['first_name', 'last_name', 'role']
list_b = ['Diego', 'Leiton', 'Software Engineer']

person = {}
index = 0
for i in range(len(list_a)):
    person[list_a[i]] =  list_b[index]
    index += 1

print(person)