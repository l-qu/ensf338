import sys
sys.setrecursionlimit(20000)

def merge_sort(data, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(data, low, mid)
        merge_sort(data, mid + 1, high)
        merge(data, low, mid, high)

def merge(data, low, mid, high):
    index_1 = mid - low + 1         # setting the lower half of the array
    index_2 = high - mid            # setting the upper half of the array
    
    left = [0] * index_1            # Low temporary arrays
    right = [0] * index_2           # High temporary arrays
    
    # Copying values from data into their left and right sides respectivelt
    for i in range(index_1):
        left[i] = data[low + i]  
    for j in range(index_2):
        right[j] = data[mid + 1 + j] 

    j = i = 0                          # Initializing i and j to 0 again
    k = low
    
    # merging the temporary arryas back in order
    while i < index_1 and j < index_2:
        if left[i] <= right[j]:         # Comparing the left and right sides and placing the smaller value into data[k]
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1   
        k += 1

    while i < index_1:                  # remaining elements copied back into left and right
        data[k] = left[i]
        i += 1
        k += 1

    while j < index_2:
        data[k] = right[j]
        j += 1
        k += 1
    print(f"Left side: {left}")  
    print(f"Right side: {right}\n")

data = [8, 42, 25, 3, 3, 2, 27, 3]

print(f"Original array is: {data}")

merge_sort(data, 0, len(data) - 1)

print(f"Sorted array is: {data}")
