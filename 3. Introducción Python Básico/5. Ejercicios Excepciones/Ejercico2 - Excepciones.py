

def menu():

    while True:
        try:
            element = int(input('How many elements do you want to evaluated: '))
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


def parser_to_int(strings_list: list):
    print('Result: ')

    for i in strings_list:

        try:

            cleaned_i = i.strip("'\"")

            print(f'"{i}" parsed to {int(cleaned_i)}')


        except ValueError:
            print(f"Unable to convert element' {i}'")




def main():

    list_ = get_list_of_string()

    parser_to_int(list_)


if __name__ == '__main__':
	main()