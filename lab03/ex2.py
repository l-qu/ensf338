import numpy as np
from random import randint
import matplotlib.pyplot as plt

def bubble_sort(arr):
    for i in range(len(arr)):
        no_swap_occurred = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                no_swap_occurred = False
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            
        if no_swap_occurred:
            break
    return arr

# helper method for median_pivot_index
# returns the index with the bigger value in the array
def bigger(arr, first, second):
    if (arr[first] > arr[second]):
        return first
    
    return second

# helper method for quicksort
# returns index of the median value
def median_pivot_index(arr, low, high):
    mid = (low + high) // 2

    biggesti = bigger(arr, low, bigger(arr, mid, high))

    if (biggesti == low):
        return bigger(arr, mid, high)
    
    if (biggesti == mid):
        return bigger(arr, low, high)
    
    return bigger(arr, low, mid)

# partition method to be used in quicksort
# arr: array to be sorted
# low and high are indices of the array, giving a range for a subarray to be sorted
# return the index of the pivot after sorting
def partition(arr, low, high):
    # choose pivot using median of three method
    pivoti = median_pivot_index(arr, low, high)

    # swap pivot to the end to get it out of the way
    temp = arr[high]
    arr[high] = arr[pivoti]     # now arr[high] holds the pivot 
    arr[pivoti] = temp

    i = low - 1                 # keep track of current index

    # loop through indices low to (high - 1)
    # swap smaller elements to the left
    for j in range(low, high):
        if (arr[j] < arr[high]):
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    
    # move pivot back to the right of the smaller elements
    temp = arr[high]
    arr[high] = arr[i + 1]
    arr[i + 1] = temp

    return i + 1

def quick_sort(arr, low=0, high=None):
    # default value
    if (high == None):
        high = len(arr) - 1

    if (low < high):
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

