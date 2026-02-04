import timeit
from random import randint
import matplotlib.pyplot as plt
import numpy as np

def linear_search(data, target):
    length = len(data)

    for i in range(length):
        if data[i] == target:
            return i
    
    return -1

def binary_search(data, target):
    high = len(data) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2

        if data[mid] == target:
            return mid
        
        if data[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1

    return -1

run_numbers = [1000, 2000, 4000, 8000, 16000, 32000]
# testing = binary_search(sorted_data, sorted_data[randint(0, 5)])
# print(f"{sorted_data[testing]}")
repeat_runs = 1000
number_runs = 100

time_linear_all = []
time_linear_average = 0
for i in range(6):
    time_linear = timeit.repeat(lambda: linear_search(list(range(run_numbers[i])), randint(0, run_numbers[i])), repeat=repeat_runs, number=number_runs)
    time_linear_all.append(time_linear)
    
    for j in range(len(time_linear) - 1):
        time_linear_average += time_linear[j]
    
    print(f"The average time taken for the linear search to find a point in an array of {run_numbers[i]} is: {time_linear_average / 1000}")
    time_linear_average = 0

# for i in range(6):
#     plt.scatter(range(1000), time_linear_all[i])
#     plt.title("Linear Graph")
#     plt.xlabel("Number of inputs")
#     plt.ylabel("Time (seconds)")
#     plt.show()

print("\n", "-" * 100, "\n")

time_binary_all = []
time_binary_average = 0
for i in range(6):
    time_binary = timeit.repeat(lambda: binary_search(list(range(run_numbers[i])), randint(0, run_numbers[i])), repeat=repeat_runs, number=number_runs)
    time_binary_all.append(time_binary)
    
    for j in range(len(time_binary) - 1):
        time_binary_average += time_binary[j]
    
    print(f"The average time taken for the binary search to find a point in an array of {run_numbers[i]} is: {time_binary_average / 1000}")
    time_linear_average = 0


# plt.scatter(range(1000), time_binary)
# plt.title("Binary Graph")
# plt.xlabel("Number of inputs")
# plt.ylabel("Time (seconds)")
# plt.show()