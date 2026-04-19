
# check is array is sorted
def isSorted(nums):
    is_sorted = True
    i = 0
    j = 1

    # while j <= len(nums)-1:
    #     if nums[i] > nums[j]:
    #         is_sorted = False
    #     i+=1
    #     j+=1
    # return is_sorted

    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            is_sorted = False
            break
    return is_sorted


def remove_dups(nums):
    num_set = set()
    for ele in nums:
        num_set.add(ele)
    i = 0 
    for ele in num_set:
        nums[i] = ele
        i+=1
    return nums

def remove_dups_optimized(nums):
    i = 0
    j = 1
    while j <= len(nums)-1:
        if nums[j] > nums[i]:
            nums[i+1] = nums[j]
            i += 1
        j +=1
    return i+1


def max_consecutive_ele(nums):
    count = 0
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
    return maxi

# Array Rotations

#time complexity: O(n)
# space complexity (extra used): O(1)
# total space used : O(n)
def left_rotate_arr_by_one(nums):
    if not nums:
        return []
    
    first = nums[0]
    for i in range(1,len(nums)):
        nums[i-1] = nums[i]

    nums[len(nums)-1] = first
    return nums


def lef_rotate_arr_by_k(nums, k):
    for i in range(k):
        nums = left_rotate_arr_by_one(nums)

    return nums


def left_rotate_arr_by_k_optimized_slicing(nums,k):
    print(nums[-1])
    k = k % len(nums)
    return  nums[k:] + nums[:k]


def left_rotate_arr_by_k_optimized(nums, k):
    num_len = len(nums)
    k = k % num_len

    temp = nums[:k]
    for i in range(k, num_len):
        nums[i-k] = nums[i]
    
    for i in range(num_len-k, num_len):
        nums[i] = temp[i - (num_len-k)]
    return nums



def right_rotate_arr_by_k(nums, k):
    k = k % len(nums)
    for j in range(k):
        last = nums[-1]
        i = len(nums)-2
        while i >= 0:
            nums[i+1] = nums[i]
            i -= 1
        nums[0] = last
    return nums

def right_rotate_arr_by_k_optimized_slicing(nums,k):
    k = k % len(nums)
    return  nums[k:] + nums[:k]


def right_rotate_arr_by_k_optimized(nums,k):
    num_len = len(nums)
    k = k % num_len

    temp = nums[-k:]
    for i in range(num_len-k-1, -1, -1):
        nums[i + k] = nums[i]
    
    for i in range(k):
        nums[i] = temp[i]
    
    return nums
    
# move 0's to end

def move_0s_to_end_brute(nums):
    # 1. Copy all the non zero elements to temp arr
    # 2. Copy the temp arr to main arr starting with 0
    # 3. Fill all the other elems in the arr with 0s. Temp arr len will be the starting index
    pass

def move_0s_to_end_optimal(nums):
    if not nums:
        return nums
    
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == 0:
            if nums[j] != 0:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
        else:
            i += 1
            j += 1
    return nums



# k = int(input())
nums = [int(n) for n in input().split()]
print(move_0s_to_end_optimal(nums))


