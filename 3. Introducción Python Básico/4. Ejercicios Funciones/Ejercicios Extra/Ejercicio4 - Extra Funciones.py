



string_value = str(input('Enter a string: '))

def counter_of_vowels(string_value):

    vowels = ['A', 'E', 'I' , 'O' ,'U']
    counter = 0

    for i in string_value:
        if i.upper() in vowels:
            counter +=1

    print('Total of vowels', counter) 

counter_of_vowels(string_value)