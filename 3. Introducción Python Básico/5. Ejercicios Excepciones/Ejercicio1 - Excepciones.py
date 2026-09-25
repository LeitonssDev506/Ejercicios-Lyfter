

def ask_for_user_information():
    try:
        name = input('Type your name: ')
        if name.isdigit():
            raise ValueError()
        print(f'Your name is: {name}')
    except ValueError as e:
        print('Your name should be a text, do not use numbers')
        raise e

    try:
        age = int(input('Type your age: '))
        if age < 10 or age > 100:
            raise ValueError()
    except ValueError as e:
        print("Invalid Age, should be >10 and less than 100!")
        raise e

    return name, age


def main():
    try:
        n, a = ask_for_user_information()
        print(f'Hola {n}, your age is {a}')
    except Exception:
        exit()


if __name__ == '__main__':
    main()