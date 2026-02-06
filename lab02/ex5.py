import timeit
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit

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
        if data[mid] > target:
            high = mid - 1   
        elif data[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1

run_numbers = [1000, 2000, 4000, 8000, 16000, 32000]
repeat_runs = 1000
number_runs = 100
lists = [list(range(n + 1)) for n in run_numbers]

time_linear_average_all = []
time_linear_average = 0
for i in range(6):
    time_linear = timeit.repeat(lambda: linear_search(lists[i], randint(0, run_numbers[i])), repeat=repeat_runs, number=number_runs)
    time_linear_average = sum(time_linear) / len(time_linear)
    time_linear_average_all.append(time_linear_average)
    print(f"Time for linear average of {run_numbers[i]} data size is: {time_linear_average}")
    time_linear_average = 0

y = np.array(time_linear_average_all)
x = np.array(run_numbers)

x_dense_grid_linear = np.linspace(min(x), max(x), 200)
linear_interp = interp1d(x, y, kind = "linear")
linear_y = linear_interp(x_dense_grid_linear)

plt.scatter(x, y)
plt.plot(x_dense_grid_linear, linear_y, label = "Linear Interpolation", linestyle = "--")
plt.legend()
plt.title("Linear Search Interpolation Graph")
plt.xlabel("Number of averages (1000-32000 pieces of data)")
plt.ylabel("Time (seconds)")
plt.show()

print("\n", "-" * 100, "\n")

time_binary_average_all = []
time_binary_average = 0
for i in range(6):
    time_binary = timeit.repeat(lambda: binary_search(lists[i], randint(0, run_numbers[i])), repeat=repeat_runs, number=number_runs)
    
    time_binary_average = sum(time_binary) / len(time_binary)
    time_binary_average_all.append(time_binary_average)
    print(f"The average time taken for the binary search to find a point in an array of {run_numbers[i]} is: {time_binary_average}")
    time_binary_average = 0

def log_func(x, a, b):
    return a * np.log(x) + b

x_binary = np.array(run_numbers)
y_binary = np.array(time_binary_average_all)
params, covariance = curve_fit(log_func, x_binary, y_binary)
a_optimal, b_optimal = params
x_dense_binary = np.linspace(min(run_numbers), max(run_numbers), 200)
y_fit_binary = log_func(x_dense_binary, a_optimal, b_optimal)

plt.scatter(x_binary, y_binary)
plt.plot(x_dense_binary, y_fit_binary, label = "Binary Interpolation", linestyle = "--")
plt.legend()
plt.title("Binary Search Interpolation Graph")
plt.xlabel("Number of averages (1000-32000 pieces of data)")
plt.ylabel("Time (seconds)")
plt.show()

# 4: 