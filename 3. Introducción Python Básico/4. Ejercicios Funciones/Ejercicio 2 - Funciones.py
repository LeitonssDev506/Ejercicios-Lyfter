
value_1 = 10

def my_sum():
    global value_1
    value_1  = 5
    value_2 = 6
    result = value_1 + value_2

    print("Result of the sum:", result)
    print("Inside the function:", value_1)

my_sum()

print("Ouf of function:", value_1) 

print("Out of the function:", value_2) # It's no possible to access a variable inside the function
