


my_list = [10, 20, 30, 40, 50]
new_list = []

sum_numbers = 0
counter = 0

for i in my_list:
    sum_numbers +=i
    counter +=1

average = (sum_numbers // counter)

for i in my_list:
    if i > average:
        new_list.append(i)

print("Average: ", average)
print("New list: ", new_list)



