def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_of_scores = 0
    sum_of_weights = 0

    for score, weight in my_list:
        sum_of_scores += score * weight
        sum_of_weights += weight

    return sum_of_scores / sum_of_weights
