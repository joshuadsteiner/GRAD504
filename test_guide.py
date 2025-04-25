# test_guide.py

# A module to centrally define the test phase information
    
def get_train_start(phase):
    start_dates = {1:'2013-01-01',
                   2:'2014-01-01',
                   3:'2015-01-01',
                   4:'2016-01-01',
                   5:'2017-01-01'}            
    return start_dates.get(phase)
