
n = 0
my_list = []
max_number = 0
while  n <=9:
    numbers = int(input("Enter a number: "))
    my_list.append(numbers)
    n +=1

for i in my_list: #
    if i >= max_number: 
        max_number = i

print( f"{my_list} The higher number was {max_number}")






