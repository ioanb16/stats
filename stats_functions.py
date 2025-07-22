def mean(a_list):
    return sum(a_list)/len(a_list)

def med(a_list):
    sorted_list = sorted(a_list)
    if len(sorted_list)%2 ==1:
        middle = len(sorted_list)/2
        return sorted_list[middle]
    m1 = (len(sorted_list)-1)/2
    m2 = (len(sorted_list)+1)/2
    return (sorted_list[m1] + sorted_list[m2])/2