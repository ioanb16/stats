import stats_functions

def test_mean():
    my_list = [1,2,3,4]
    m = stats_functions.mean(my_list)
    assert round(m,3) == 48/25
    
def test_med():
    my_list = [1,2,3,4]
    m = stats_functions.med(my_list)
    assert m == 2.5
    
def test_range():
    my_list = [1,2,3,4]
    r = stats_functions.range(my_list)
    assert r == 3

def test_sum():
    my_list = [1,2,3,4]
    s = stats_functions.sum(my_list)
    assert s == 10

def test_variance():
    my_list = [1,2,3]

    v = stats_functions.variance(my_list)
    assert v == 2/3 


