import random
import numpy as np
from matplotlib import pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if(arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swaps += 1
    return comparisons, swaps

sizes = [10, 20, 30, 40, 50, 70, 100, 150, 200]
runs = 20
avg_comparisons = []
avg_swaps = []

for n in sizes:
    total_comparisons = []
    total_swaps = []
    for i in range(runs):
        arr = random.sample(range(n * 10), n)
        comparisons, swaps = bubble_sort(arr.copy())
        total_comparisons.append(comparisons)
        total_swaps.append(swaps)
    avg_comparisons.append(np.mean(total_comparisons))
    avg_swaps.append(np.mean(total_swaps))

n_vals = np.array(sizes)
theoretical_comparisons = n_vals * (n_vals - 1) / 2
theoretical_swaps = n_vals * (n_vals - 1) / 4

plt.figure()

plt.subplot(1, 2, 1)
plt.plot(sizes, avg_comparisons, 'o-', label="Measured")
plt.plot(sizes, theoretical_comparisons, '--', label="n(n-1)/2")
plt.xlabel("Input size n")
plt.ylabel("Number of comparisons")
plt.title("Comparisons")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(sizes, avg_swaps, 'o-', label="Measured")
plt.plot(sizes, theoretical_swaps, '--', label="n(n-1)/4")
plt.xlabel("Input size n")
plt.ylabel("Number of swaps")
plt.title("Swaps")
plt.legend()

plt.show()