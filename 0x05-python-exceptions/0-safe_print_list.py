#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if count < x:
                print(element, end="")
                count += 1
            else:
                break
        print()
        return count
    except:
        pass


# Test cases
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print:", nb_print)

nb_print = safe_print_list(my_list, len(my_list))
print("nb_print:", nb_print)

nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print:", nb_print)
