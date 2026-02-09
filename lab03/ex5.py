def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def binary_insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = binary_search(data)
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def binary_search(data, target, low, high):
    while low <= high:
        mid = (low + (high - low)) // 2
        if data[mid] > target:
            high = mid - 1   
        elif data[mid] < target:
            low = mid + 1
        else:
            return mid
    return low