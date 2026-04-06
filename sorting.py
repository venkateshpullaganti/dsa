import math
def get_min(arr):
    min = arr[0]
    i = 0
    index = 0
    while i < len(arr):
        if arr[i] < min:
            min = arr[i]
            index = i
        i = i+1
    return min, index


# Time complexity : O(~n^2)
def selection_sort(arr):
    for i in range(len(arr)-1): # n 
        min, index = get_min(arr[i:]) # ~n
        arr[i], arr[index+i] = min, arr[i]
    print(arr)


# Time complexity : O(~n^2)
def bubble_sort(arr):
    for i in range(len(arr)-1):
        left = 0
        right = 1
        while right < len(arr)-i:
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right],arr[left]
            print(left, right)
            left = left + 1
            right = right + 1
    print(arr)


# Time complexity : O(~n^2)
# Best Time complexity: O(n) if already sorted asc order
def bubble_sort_optimized(arr):
    for i in range(len(arr)-1):
        left = 0
        right = 1
        did_swap = False
        while right < len(arr)-i:
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right],arr[left]
                did_swap = True
            left = left + 1
            right = right + 1
        if not did_swap:
            break
    return arr



# Time complexity : O(~n^2)
# worst and avg case : O(~n^2)
# best case : O(n) no swap if already sorted.
def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j],arr[j-1]
            j = j - 1
    print(arr)




def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left = left + 1
        else:
            temp.append(arr[right])
            right = right+1
    
    while left <= mid:
        temp.append(arr[left])
        left = left+1
    
    while right <= high:
        temp.append(arr[right])
        right = right + 1
    
    i = low
    while i <= high:
        arr[i] = temp[i - low]
        print(f"swap {i-low}")
        i = i+1


# Time complexity: O(nlogn) (best, avg, worst cases)
# Space complexity: O(n)
def merge_sort(arr, low, high):
    if low >= high:
        return arr
    
    mid = (low+high)//2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)
    print(arr)
    return arr

n = [int(i) for i in input().split(" ")]

print(merge_sort(n,0,len(n)-1))