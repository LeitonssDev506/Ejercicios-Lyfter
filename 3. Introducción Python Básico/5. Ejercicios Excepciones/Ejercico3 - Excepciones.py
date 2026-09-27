

def menu():

    while True:
        try:
            element = int(input('How many elements do you want to evaluate: '))
            if 1 <= element <= 100:
                return element
            print('Error: Please enter a number between 1 and 100.')
        
        except ValueError:
            print("Error: Invalid number. Please try again.")



def get_list_of_string():
    list_of_string = []

    e = menu()

    for e in range(0,e):
        s = input("Type: ")
        list_of_string.append(s)


    return list_of_string


def sum_values(strings_list: list):
    total = 0

    for i in strings_list:
        try:
            cleaned_i = float(str(i).strip("'\""))
            print(f'{cleaned_i} added successfully')
            total += cleaned_i
        except ValueError:
            print(f'Invalid element: {i}')

    print(f'Total added: {total}')



def main():

    list_ = get_list_of_string()

    sum_values(list_)


if __name__ == '__main__':
	main()