import timeit

def sub_function(n):
    if n==0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    return [i**2 for i in range(100000000)]

test_function()
third_function()