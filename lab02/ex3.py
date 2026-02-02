import timeit
import cProfile

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

# 1. A profiler analyzes a program's runtime performance by measuring where the most time is being spent
# 2. Benchmarking measures how long a program or a section of a program takes to run, 
# while profiling determines where that time is being spent within the program. Both are used to analyze a program's peformance, 
# but benchmarking is coarse grained information while profiling is fine-grained. 