
text = str(input('Type a text: '))
character = str(input('Type a character that want to search: '))

def count_string(text, character):


    counter = 0
    for t in text:
        if t == character:
            counter+=1

    print(f'We founded {counter} times the character')



count_string(text, character)


