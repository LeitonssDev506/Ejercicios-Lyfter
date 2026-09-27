my_list = ["cielo", "sol", "maravilloso", "día"]

number_of_letters = int(input('Enter a minimum of letter to search '))


def select_more_than_n_words(my_list: list , number_of_letters: int):

    list_of_words = []
    for i in list(range(len(my_list))):
        if len(my_list[i]) > number_of_letters:
            list_of_words.append(my_list[i])

    print(list_of_words)


select_more_than_n_words(my_list, number_of_letters)