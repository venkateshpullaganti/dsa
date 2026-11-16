#   --------------------- Searching an element ---------------

def binary_search_loops(nums,target):
    low = 0
    high = len(nums)-1
   

    while low <= high:
        mid = (low+high)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid-1

    return -1 

def binary_search_recursion(nums, target, low, high):
    if low <= high:
        mid = (low + high)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return binary_search_recursion(nums,target,  low, mid-1)
        else:
            return binary_search_recursion(nums, target,  mid+1, high)
    return -1


nums = [int(n.strip()) for n in input().split(",")]
k = int(input())
l = len(nums)


nums = [int(n.strip()) for n in input().split(",")]
k = int(input())
l = len(nums)

print(binary_search_recursion(nums, k, 0, l-1))