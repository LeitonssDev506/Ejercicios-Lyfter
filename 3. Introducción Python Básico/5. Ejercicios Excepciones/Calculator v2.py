def display_menu():
    print(50 * '-')
    print('This is a Basic Calculator')
    print(50 * '-')
    print('Select an option to do an operation:\n')
    print('1. Add ➕')
    print('2. Subtract ➖')
    print('3. Multiply ✖️')
    print('4. Divide ➗')
    print('5. Clear the result 🆑')
    print('6. Close the calculator 🔒\n')
 
 
def type_new_number(prompt="Type a number: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid number. Please try again.")
 
 
def get_menu_option():
    while True:
        try:
            option = int(input('Type a number from 1 to 6: '))
            if not (1 <= option <= 6):
                raise ValueError("Option out of range.")
            return option
        except ValueError:
            print("Error: Invalid option. Please enter an integer between 1 and 6.")
 
 
def add(current, number):
    return current + number
 
 
def subtract(current, number):
    return current - number
 
 
def multiply(current, number):
    return current * number
 
 
def divide(current, number):
    return current / number
 
 
def divide_with_retry(current):
    while True:
        number = type_new_number("Type number to divide by: ")
        try:
            return divide(current, number)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please try another number.")
 
 
def main():
    current_number = 0.0
 
    while True:
        display_menu()
        option = get_menu_option()
 
        if option == 6:
            print("\nClosing calculator. Goodbye!")
            break
 
        print(f'Current number: {current_number}')
 
        match option:
            case 1:
                number = type_new_number("Type number to add: ")
                current_number = add(current_number, number)
                print(f"Result: {current_number}")
 
            case 2:
                number = type_new_number("Type number to subtract: ")
                current_number = subtract(current_number, number)
                print(f"Result: {current_number}")
 
            case 3:
                number = type_new_number("Type number to multiply: ")
                current_number = multiply(current_number, number)
                print(f"Result: {current_number}")
 
            case 4:
                current_number = divide_with_retry(current_number)
                print(f"Result: {current_number}")
 
            case 5:
                current_number = 0.0
                print("Result cleared to 0.0")
 
 
if __name__ == '__main__':
    main()