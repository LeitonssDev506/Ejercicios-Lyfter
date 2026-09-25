
numbers = list()
n = 1
while n <= 3:
    num = int(input("Enter a number: "))
    numbers.append(num)
    n+= 1

if numbers[0] == 30 or numbers[1] == 30 or numbers[2] == 30:
    print(f"Correct there are a 30 in the list: {numbers}")

elif sum(numbers) == 30:
    print(f"Correct the sum of the numbers is 30: {numbers}")

else:
    print(f"Incorrect there are no 30 in the list at the sum isn't 30: {numbers}")
        
        