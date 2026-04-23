
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

# keep on comparing with nums[i] and if greater then place it at i+1 and incrent i 
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

def find_missing_number_brute(nums, n):
    """
        From 1 to n, Search the array every time and if not found
        return that number
     """
    for i in range(1,n+1):
        exists = False
        for j in nums:
            if j == i:
                exists = True
        if not exists:
            return i    


def find_missing_number_better(nums):
    """
    Create a hash map and mark the numbers, at end return that number
    that is not repeated.
    """
    hash_nums = [0 for i in range(0,len(nums)+1)]

    for num in nums:
        hash_nums[num] = 1
    
    for i in range(len(hash_nums)):
        if hash_nums[i] == 0:
            return i
        

def find_missing_number_optimal_1(nums):
    """
    Find the sum of n natural nums and sum the nums in arr
    subtract you will get the missing num
    
    """
    nums_len = len(nums)+1
    s = (nums_len * (nums_len-1))//2

    for n in nums:
        s = s - n
    return s

def find_missing_number_optimal_2(nums):
    """
    Compute the xor for array
    
    """
    xor1= 0
    xor2 = 0
    for i in range(len(nums)):
        print(i)
        xor1 ^= i + 1
        xor2 ^= nums[i]

    return xor1^xor2



def union_of_2_sorted_arrays(nums1, nums2):
    uset = set()
    union = []

    for n in nums1:
        uset.add(n)        

    for n in nums2:
        uset.add(n)

    for n in sorted(uset):
        union.append(n)
    return union


def union_of_2_sorted_arrays_optimal(nums1, nums2):
    """
    Two pointer approach

    Time Complexity: O(M+N), because both the arrays must be traversed once.
    Space Complexity: O(M+N), considering the space for returning the output, which in the worst case, can contain all the elements from both arrays.
    """
    union = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            s = nums2[j]
            j += 1
        else:
            i += 1
        if not union or s > union[-1]:
            union.append(s)
    
    while i < len(nums1):
        if union[-1] < nums1[i]:
            union.append(nums1[i])
        i+=1

    while j < len(nums2):
        if union[-1] < nums2[j]:
            union.append(nums2[j])
        j += 1
    
    return union



# k = int(input())
nums = [int(n) for n in input().split()]
nums2 = [int(n) for n in input().split()]

print(union_of_2_sorted_arrays_optimal(nums,nums2))


