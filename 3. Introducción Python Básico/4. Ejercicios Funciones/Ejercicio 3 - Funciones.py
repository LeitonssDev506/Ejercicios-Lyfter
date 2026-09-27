
list_ = [4, 6, 2, 29]


def sum_all_values(values_):
    variable = 0
    for i in values_:
        variable += i

    return variable


total = sum_all_values(list_)


print(f"Sum of the list {list_} is → {total}")