def mean(a_list):
    return sum(a_list)/len(a_list)

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
