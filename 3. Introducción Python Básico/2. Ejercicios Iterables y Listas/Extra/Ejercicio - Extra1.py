

my_list = [4,3,7,2,8,2,1,3,3,3,3]

number = int(input("Enter a number: "))


counter = 0
for i in my_list:
    if i == number:
        counter +=1

print(f"The number {number} shows up {counter} times")