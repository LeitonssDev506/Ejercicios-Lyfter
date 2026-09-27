my_list = [4, 3, 6, 1, 7]


temporal_number_last_position = my_list[(len(my_list)-1)]
temporal_number_first_position = my_list[0]

my_list[(len(my_list)-1)] = temporal_number_first_position
my_list[0] = temporal_number_last_position

print(my_list)