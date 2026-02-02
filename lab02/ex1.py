import timeit
import matplotlib.pyplot as plt
import numpy as np

# 1. This code calculates the nth term of the fibonacci sequence.

# 2. Although this code isn't the most efficient, it is an example of a divide and
#    conquer algorithm because it splits the problem into smaller subproblems,
#    solves them separately, and combines them to find the solution.

# 3. Time complexity is O(2^n).

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n - 1) + func(n - 2)

# 4.   
def funcBetter(n):
    cache = [None]*(n + 1)
        
    if n == 0 or n == 1:
        return n
    
    if cache[n] != None:
        return cache[n]

    cache[n] = funcBetter(n - 1) + funcBetter(n - 2)
    return cache[n]

# 5. The new time complexity is O().

# 6.
input = []
times = []

for i in range(36):
    time = timeit.timeit(lambda: func(i), number=1)
    input.append(i)
    times.append(time)

plt.scatter(input, times)
plt.title("Original function")
plt.xlabel("Number of inputs")
plt.ylabel("Time (seconds)")
# plt.savefig("output1.6.1.jgp")
plt.show()

inputBetter = []
timesBetter = []

for i in range(36):
    time = timeit.timeit(lambda: funcBetter(i), number=1)
    inputBetter.append(i)
    timesBetter.append(time)

plt.clf()
plt.scatter(inputBetter, timesBetter)
plt.title("Optimized function supposedly")
plt.xlabel("Number of inputs")
plt.ylabel("Time (seconds)")
# plt.savefig("output1.6.2.jgp")
plt.show()