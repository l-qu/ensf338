import cProfile
import pstats
from io import StringIO

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

pr = cProfile.Profile()
pr.enable()
test_function()
third_function()
pr.disable()

s = StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
ps.print_stats(10)
print(s.getvalue())

# 1. A profiler analyzes a program's runtime performance by measuring where the most time is being spent
# 2. Benchmarking measures how long a program or a section of a program takes to run (ie 'how long did it take'), 
# while profiling determines where that time is being spent within the program (ie 'where did the time go'). Both are used to analyze a program's peformance, 
# but benchmarking is coarse grained information while profiling is fine-grained. 
# 4. From output: 68 function calls during profiling. third_function called once but takes up most the runtime. test_function called once, 
# sub_function called 55 total times (10 primitive calls) but both run very fast.
# The majority of the execution time goes to third_function(). It iterates over 100 million elements, computing i**2, and populating a very big list.
# The operations are fast but the function performs a massive number of repetitions.
# test_function() runs once and only loops once, sub_function is recursive but is only called a small number of times
# So the profiler shows that the execution time is mostly spent in third-function, not test-function or sub-function.
