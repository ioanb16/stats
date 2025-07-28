def harmonic_mean(a_list):
    inverse_list = [1/x for x in a_list if x != 0]
    return len(a_list) / sum(inverse_list)

def mean(a_list):
    sum_value = sum(a_list)
    return sum_value / len(a_list) 


def med(a_list):
    sorted_list = sorted(a_list)
    if len(sorted_list)%2 ==1:
        middle = len(sorted_list)/2
        return sorted_list[middle]
    m1 = int((len(sorted_list)-1)/2)
    m2 = int((len(sorted_list)+1)/2)
    return (sorted_list[m1] + sorted_list[m2])/2

def range(a_list):
    max_value = max(a_list)
    min_value = min(a_list)
    return max_value - min_value


def sum(a_list):
    sum_value = 0
    for number in a_list:
        sum_value += number
    return sum_value

def variance(a_list):
    m = mean(a_list)
    squared_diff = [(x - m) ** 2 for x in a_list]
    return mean(squared_diff)

