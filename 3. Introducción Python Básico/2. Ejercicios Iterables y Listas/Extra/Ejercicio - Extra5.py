

my_list = ['sol', 'estrella', 'luz', 'planeta', 'roca']


w = 0
words_list = []

while w <= 4:
    counter=0
    words = str(input("Type 5 words: "))

    for i in words:
        counter +=1

    if counter > 4:
        words_list.append(words)  

    w +=1


print(words_list)