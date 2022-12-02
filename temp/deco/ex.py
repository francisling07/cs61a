import trace

def trace1(fn):
    """return a version of fn that first print"""
    def traced(x):
        print('calling', fn, 'on argument',x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x*x

@trace1
def sum_square_up_to(n):
    k, total = 1, 0
    while k<= n:
        total, k = total + square(k), k+1
    return total
