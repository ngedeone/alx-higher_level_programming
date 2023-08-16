#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    sum = 0

    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.add(num)
            sum += num

    return sum
