my_string = "Pizza con piña"


def reverse_the_string(text_of_string):
    final_string = ""


    for i in range(len(text_of_string) - 1, -1, -1):
        final_string = final_string + text_of_string[i]

    return final_string



reversed_result = reverse_the_string(my_string)

print(f"{my_string} → {reversed_result}")