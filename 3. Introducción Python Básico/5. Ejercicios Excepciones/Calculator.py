

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

initial_number = 0.0
option = 0

while option != 6:
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


    option = get_menu_option()

    print(f'Current number: {initial_number}')

    if option == 6:
        print("\nClosing calculator. Goodbye!")
        break

    match option:
        case 1:
            number = type_new_number("Type number to add: ")
            initial_number += number
            print(f"Result: {initial_number}")

        case 2:
            number = type_new_number("Type number to subtract: ")
            initial_number -= number
            print(f"Result: {initial_number}")

        case 3:
            number = type_new_number("Type number to multiply: ")

            if initial_number == 0.0:
                initial_number = number
            else:
                initial_number *= number
            print(f"Result: {initial_number}")

        case 4:
            while True:
                try:
                    number = type_new_number("Type number to divide by: ")
                    initial_number /= number
                    print(f"Result: {initial_number}")
                    break
                except ZeroDivisionError as e:
                    print(f"Error: Cannot divide by zero. Try another number {e}")
            

        case 5:
            initial_number = 0.0
            print("Result cleared to 0.0")







    



