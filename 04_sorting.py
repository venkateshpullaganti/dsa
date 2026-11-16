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



def rec_bubble_sort(arr, current = 0):
    if current >= len(arr)-1:
        return arr
    left = 0
    right = 1
    while right < len(arr)-current:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        left = left+1
        right = right + 1
    return rec_bubble_sort(arr, current+1)



def rec_insertion_sort(arr, current = 0):
    if current >= len(arr)-1:
        return arr
    i = current
    min_index = i
    while i <= len(arr)-1:
        if arr[i] < arr[min_index]:
            min_index = i
        i = i+1
    arr[current], arr[min_index] = arr[min_index], arr[current]
    return rec_insertion_sort(arr, current+1)



def partition(arr, low, high):
    pivot = arr[low]

    i = low
    j = high
    
    while i < j:
        while i <= high-1 and arr[i] <= pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1
        
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], pivot
    return j
 

def quick_sort(arr, low, high):
    if low > high:
        return arr
    
    p_index = partition(arr, low, high)
    quick_sort(arr, low, p_index - 1)
    quick_sort(arr,  p_index + 1, high)

    return arr



n = [int(i) for i in input().split(" ")]

print(quick_sort([], 0, len([])-1))

