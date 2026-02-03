def linear_search(data, target):
    length = len(data)

    for i in range(length):
        if data[i] == target:
            return i
    
    return -1

def binary_search(data, target):
    high = len(data) 
    low = 0

    while high >= low:
        mid = (low + (high - low)) // 2

        if data[mid] == target:
            return mid
        
        elif data[low] == target:
            return low
        
        elif data[high] == target:
            return high
    
    return -1

sorted_data = [1000, 2000, 4000, 8000, 16000, 32000]

print(f"this was found at binary index: {binary_search(sorted_data, 8000)}")
print(f"this was found at linear index: {linear_search(sorted_data, 8000)}")