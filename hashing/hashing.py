# ---------------- Longest consecutive sequence ------------

def linear_search(x, nums):
    for num in nums:
        if num == x:
            return True
    return False

def longest_consq_seq_brute(nums):
    """
        Pick an element from start and search for the next conseq elements till no one found.
        Then count and return the highest count.

        Time Complexity: O(N^3), as 3 nested loops
        Space: O(1)
    
    """
    if not nums:
        return 0

    max_len = 0

    for num in nums: # loop 1 for picking element
        count = 1
        next_num = num+1
        while linear_search(next_num, nums): # While loop for continued elements search and linear_search is also a loop 
            next_num += 1
            count +=1

        if count > max_len:
            max_len = count
    return max_len


def longest_conseq_better(nums):
    """
    Sort the array, keep a counter and last_ele in the sequence,
    when current ele == last_ele+1 it is part of seq. increment count
    If ele != last_ele+1, reset count and last element.

    Time: O(NlogN) + O(N), sorting and then iterating
    Space: O(1)
    
    """
    if not nums:
        return 0
    
    nums.sort()

    print(nums)
    
    max_len = 1
    last_ele = nums[0]

    count = 1
    for num in nums:
        if last_ele+1 == num:
            count+=1
            last_ele = num
        elif last_ele != num:
            count = 1
            last_ele = num
        
        if count > max_len:
            max_len = count
    
    return max_len


def longest_conseq_optimal(nums):
    """
    Convert the list to set, and iterate over each element,
    for each element if the element-1 found in set, skip else
    assume it is the starting of seq and continue till the seq breaks.

    Time: O(N) + O(2N), for converting it into set and for finding the seq, 
    At worst it will iterate 2 times for each element. 
    Under the assumption of set lookup takes O(1) time, for worst case if set lookup takes O(NlogN) then better soln is good.

    Space: O(N), for set
    
    """
    if not nums:
        return nums
    
    nums_set = set(nums)

    max_len = 1
    for n in nums_set:
        if not n-1 in nums_set:
            count = 0
            while n in nums_set:
                n = n+1
                count+=1
            if count > max_len:
                max_len = count
    return max_len


def longest_sub_array_with_sum_k_brute1(nums, k):
    """
    Generate all the sub arrays and count the sum, when the count == k and len > current max, save in max.
    Time Complexity: O(N^3)
    Space Complexity: O(1)
    """

    if not nums:
        return 0
    
    max_len = 0

    num_len = len(nums)
    for i in range(num_len):
        for j in range(i, num_len):
            sum = 0
            for l in range(i, j+1):
                sum+= nums[l]
            if sum == k and j - i+1 > max_len:
                max_len = j-i+1
    
    return max_len

def longest_sub_array_with_sum_k_brute_2(nums, k):
    """
    Generate all the sub arrays and count the sum, when the count == k and len > current max, save in max.
    Time Complexity: O(N^3)
    Space Complexity: O(1)
    """

    if not nums:
        return 0
    
    max_len = 0

    num_len = len(nums)
    for i in range(num_len):
        sum = 0
        for j in range(i, num_len):
            sum += nums[j]
            if sum == k and j-i+1 > max_len:
                max_len = j-i+1

    return max_len

def longest_sub_array_with_sum_k_better_pos_negs_prefix_sum(nums,k):
    """
    Iterate over each element and save the sum in hash map, now
    for the sub array to exists, we need sum-k before so that from that 
    sum we get the sub array.

    Complexity: 
        Time: O(N) *  O(1) / O(N) for worst case if collisions happen.
            For ordered/sorted dict, it it will be O(N logN)
        Space:
            O(N) for saving the sums.
    """
    
    if not nums:
        return 0
    
    sums = dict()

    longest = 0
    current_sum = 0

    for i in range(len(nums)):
        
        current_sum += nums[i]

        if sums.get(current_sum,-1) == -1:
            sums[current_sum] = i

        diff = current_sum - k

        if current_sum == k and i+1 > longest:
            longest = i+1
        elif sums.get(diff, -1) != -1 :
            current_len = i - sums.get(diff)
            if current_len > longest:
                longest = current_len
        
    return longest

def longest_sub_array_with_sum_k_optimal_2_pointer(nums, k):
    """
    We take 2 pointers, left and right, we start iterating the elements and adding 
    to sum, when the sum is greater than k, then we start left pointer to increase 
    to check and reducing those nums from sum. The elements sum when equal to k, right-left is the len. 
    save the len and continue till the end.

    Complexity:

    Time: O(N), as there are two pointers traversing the arr only once. 
    Space: O(1), no extra space used.
    """
    if not nums:
        return 0

    right = 0
    left = 0
    s = nums[right]
    longest = 0

    while right < len(nums):

        while left < right and s > k:
            s -= nums[left]
            left += 1
        
        if s == k and  right-left > longest:
            longest = right-left

        right += 1
        if right < len(nums):
            s+=nums[right]
            
    return longest


def count_subarrays_with_given_sum_brute(nums, k):
    """
    Find all the sub arrays and sum and count them

    Time: O(N^3), 3 nested loops
    Space: O(1)
    """

    if not nums:
        return 0

    subs = 0

    num_len = len(nums)

    for i in range(num_len):
        for j in range(i, num_len):
            s = 0
            for l in range(i, j+1):
                s = s+nums[l]
            
            if s == k:
                subs += 1
    return subs


def count_subarrays_with_given_sum_better(nums, k):
    """
    Instead of the 3rd nested loop, we directly sum and compare in second loop itself.

    Time: O(N^2), 2 nested loops
    Space: O(1)
    """

    if not nums:
        return 0

    subs = 0

    num_len = len(nums)

    for i in range(num_len):
        s = 0
        for j in range(i, num_len):
            s+= nums[j]
            if s == k:
                subs += 1
    return subs


def count_subarrays_with_given_sum_optimal_prefix_sum(nums, k):
    """
    Store the counts and
    

    """

    if not nums:
        return 0
    
    sums= {0:1}
    count = 0
    current_sum = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        
        diff = current_sum - k

        count += sums.get(diff,0)

        sums[current_sum] = sums.get(current_sum, 0) + 1

    return count


def count_subarrays_with_given_xor_optimal(nums, k):
    """
    The idea is to find the x where x = current_xor ^ k,
    because x ^ k = current_xor, in order for k to exists there
    must be an element current_xor ^ k somewhere till current idx.

    Time: O(N), iterating only once.
    Space: O(N), for saving xors
    """
    xors = {0:1}
    sub_array_xors = 0

    current_xor = 0
    for i in range(len(nums)):
        current_xor = current_xor ^ nums[i]

        search_xor = current_xor ^ k
        sub_array_xors += xors.get(search_xor, 0)

        xors[current_xor] = xors.get(current_xor,0) + 1
        
    return sub_array_xors

nums = [int(n.strip()) for n in input().split(",")]
k = int(input().strip())
print(count_subarrays_with_given_xor_optimal(nums,k))


