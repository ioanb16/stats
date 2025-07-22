import stats_functions

def test_mean():
    my_list = [1,2,3,4]
    m = stats_functions.mean(my_list)
    assert m == 2.5
    
    