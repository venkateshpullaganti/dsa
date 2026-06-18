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


nums = [int(n.strip()) for n in input().split(",")]
print(longest_conseq_optimal(nums))