def sort_hyphen_string(text):

    word_list = text.split("-")

    word_list.sort()
    
    final_text = "-".join(word_list)
    
    return final_text

my_input = "python-variable-funcion-computadora-monitor"
result = sort_hyphen_string(my_input)

print(result)