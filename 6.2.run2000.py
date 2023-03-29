import pdb
from time import time

"""The timer function in Python measures the execution time of a given function 
by recording the start and end times and calculating their difference.
   """

def timer(func, *args, **kwargs):
    start_time = time()
    func(*args, **kwargs)
    end_time = time()
    time_of_func = end_time - start_time
    return time_of_func

