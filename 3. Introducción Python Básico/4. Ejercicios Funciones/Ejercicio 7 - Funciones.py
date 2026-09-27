

my_list = [1, 4, 6, 7, 13, 9, 67] #→ [7, 13, 67]

#my_list = [ 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]# 100 primos


def prime_not_prime_function(my_list):
    import math

    #Rules
    #The number 1 is not prime
    #The number 2 is the only par number prime
    #If any division is exact → it is NOT prime (division is exact = {Quotient}*{Divisor} = {Dividend})
    #If no division is exact → it is prime (division not exact {Quotient}*{Divisor} != {Dividend})

    list_of_number = []

    for i in my_list:

        if i <= 1:
            continue
        elif i == 2:
            list_of_number.append(i)

        elif i % 2 == 0:
            continue
        else:
            exact_division = []
            result_sqrt = int(round(math.sqrt(i),0))
            dividend = i
            

            for divisor in list(range(3, result_sqrt+1,2)):
                integer_part = dividend // divisor
                formula = (integer_part * divisor)

                if formula == dividend:
                    exact_division.append('Division Exact')
                else:
                    exact_division.append('No Division Exact')

            if 'Division Exact' in exact_division:
                continue
            else:
                list_of_number.append(i)

        
    print(f'List of prime numbers: {list_of_number}')


prime_not_prime_function(my_list)

