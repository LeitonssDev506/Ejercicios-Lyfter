
my_list = [4,3,7,2,8,2,0]

counter =0
for i in my_list:
    if i > 0:
        counter +=1

if counter == len(my_list):
    print("The numbers inside the list are positive")
else:
    print("At least one number is negative or zero.")



