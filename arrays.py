
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
    """
    Time Complexity: O( (M+N)log(M+N) ), at max set can store M+N elements {when there are no common elements and elements in nums1 , nums2 are distntict}. So Inserting M+N th element takes log(M+N) time. Upon approximation across inserting all elements in worst, it would take O((M+N)log(M+N) time.

    Space Complexity: O(M+N), considering space of Union Array.
    
    """
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


def intersection_of_two_sorted_array(nums1, nums2):
    """
    initiate two separate arrays : intersection_arr & visited_arr for nums2.
    Iterate over nums1 and if num matched with nums2[i] and is not yet taken then add to intersection arr.
    Return intersection arr.

    Edge Cases: 
        - Extra copies in 1 arr and not in other

    Time complexity: O(n) * O(m) = O(n*m) ~ O(n^2)
    Space complexity: O(2m) (intersection_arr + visited_arr)    
    """
    intersection_nums = []
    visited_nums = [0 for i in range(len(nums2))]

    for num in nums1:
        i = 0
        while i < len(nums2):
            if nums2[i] == num and visited_nums[i] == 0:
                intersection_nums.append(nums2[i])
                visited_nums[i] = 1
                break          # Once matched with any number we don't need to continue. 
            elif nums2[i] > num:
                break         # We exceeded the num in the sorted nums2 array, so all other will always be greater
            i += 1

    return intersection_nums 


def intersection_of_two_sorted_arrays_optimal(nums1,nums2):
    """
    Two pointer approach: 
    Two pointer i and j will move on respective arrays, if any number nums1[i] == nums2[j] append it to the intersection and increment both pointers
    else increment the lesser number index and continue.

    Time complexity: O(n+m)
    Space complexity: O(min(m,n))
    """
    intersection_arr = []
    i = 0
    j = 0
    while i < len(nums1) and j<len(nums2):
        if nums1[i] == nums2[j]:
            intersection_arr.append(nums1[i])
            i += 1
            j += 1
        elif nums2[j] > nums1[i]:
            i += 1
        else:
            j += 1
    return intersection_arr


### Majority Element

def majority_ele_brute(nums):
    """
    Majority element : Element that appears greater than len(nums)/2 

    Iterate over each element and find the elements counts and return if count is > n/2

    Time complexity = O(n^2)
    Space Complexity = O(1)

    """
    
    for num in nums:
        count = 0
        for num2 in nums:
            if num == num2:
                count+= 1
        
        if count > len(nums)/2:
            return num
    return -1
        
def majority_ele_better(nums):
    """
    Using Hashing, keeping the count of the num iterated over.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    hash_n = dict()
    for num in nums:
        if hash_n.get(num):
            hash_n[num] = hash_n[num] + 1
        else:
            hash_n[num] = 1
    for k,v in hash_n.items():
        if v > len(nums)/2:
            return k
    return -1

def majority_ele_optimal_moors_voting_algo(nums):
    """
    Moor's Voting Algorithm:
        Consider any element as the majority element and iterate through the arr.
        If current num == ele then increase the count else decrease, if counter resets to 0, then take the fresh element and start.

    Time complexity: O(n) + O(n)
    Space complexity: O(1)
    """

    ele = 0
    count = 0

    for num in nums:
        if count == 0:
            ele = num
            count += 1
        elif ele == num:
            count+=1
        else:
            count-=1
    
    count2 = 0
    for num in nums:
        if num == ele:
            count2+=1
    if count2 > len(nums)/2: # only verify if they say arr might not contain majority ele 
        return ele

    return -1



# Leaders in the array

def leaders_in_arr_brute(nums):
    """
    Iterate over each element and compare with next elements. 
    
    Time complexity: O(n^2)
    Space complexity: O(1) # not used any space to solve the problem but used to store it. If you consider it will be O(n)
    """

    leaders = []
    for i in range(len(nums)):
        j = i + 1
        is_leader = True
        while j < len(nums):
            if nums[j] >= nums[i]:
                is_leader = False
                break
            j+=1
        if is_leader:
            leaders.append(nums[i])
    
    return leaders

def leaders_in_arr_optimal(nums):
    """
    Traverse the array from right and save the largest ele and keep on comparing with previous
    and if the current is larger than largest ele then it is one of the leader.

    Time complexity: O(n) or O(N logN) if asked to return the sorted.
    Space complexity: O(n) just 
    
    """
    largest = nums[len(nums)-1]
    leaders = [largest]
    
    for i in range(len(nums)-1,-1, -1):
        if nums[i] > largest:
            leaders.append(nums[i])
            largest = nums[i]

    leaders.reverse()
    return leaders


def rearrange_ele_by_sign_brute(nums):
    """
        Time complexity: O(n) + O(n/2)
        Space complexity: O(n)
    """
    pos = []
    neg = []

    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    
    for i in range(len(nums)//2):
        nums[2*i] = pos[i]
        nums[2*i+1] = neg[i]
    
    return nums

def rearrange_ele_by_sign_optimal(nums):
    """
    Time complexity = O(n)
    Space complexity = O(n)
    
    """
    arranged = [0 for i in range(len(nums))]

    pos_index = 0
    neg_index = 1

    for num in nums:
        if num > 0:
            arranged[pos_index] = num
            pos_index += 2
        else:
            arranged[neg_index] = num
            neg_index += 2
    return arranged


def print_spiral_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    left = 0
    right = m-1
    top = 0
    bottom = n-1

    spiral = []

    while top <= bottom and left <= right:
        # right
        for i in range(left, right+1):
            spiral.append(matrix[top][i])
        
        top+=1

        # bottom
        for i in range(top, bottom+1):
            spiral.append(matrix[i][right])
        
        right-=1

        if top <= bottom:
             # left
            for i in range(right, left-1, -1):
                spiral.append(matrix[bottom][i])
            bottom -=1

        if left <= right:
            # top
            for i in range(bottom, top-1, -1):
                spiral.append(matrix[i][left])
            left+=1

    return spiral




# Pascals Triangle

"""
Pascals Triangle: 


"""


def calc_number_at_position_pascals_triangle(n,r):
    """
    Use nCr formula : n!/r!*(n-r)!

    if we solve above eq it comes down to 
    """
    res = 1

    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res


def print_rth_row_pascal_triangle(r):
    """
    Time complexity : O(n)
    
    """
    ans = [0] * r
    ans[0] = 1
    for i in range(1,r):
        ans[i] = (ans[i-1] * (r-i)) // i
    return ans


def return_pascal_triangle(r):
    ans = []
    for i in range(1,r+1):
        temp = [0] * i
        temp[0] = 1
        for j in range(1,i):
            temp[j] = (temp[j-1] * (i-j)) // j
        ans.append(temp)
    return ans

def rotate_matrix_by_90(arr):
    """
    Time complexity : O(n^2)
    Space complexity : O(n^2)
    """
    n = len(arr)
    m = len(arr[0])

    temp =[ [0] * n for i in range(n)]

    for i in range(n):
        for j in range(m):
          temp[j][(n-1)-i] = arr[i][j]

    return temp


def rotate_matrix_optimal(arr):
    """
    Transpose and reverse. 
    Transpose: Reverse the elements except the diagonal ones

    Time complexity: O(2n^2)
    Space complexity: O(1)
    """

    n = len(arr)
    m = len(arr[0])

    # Transpose the matrix
    for i in range(n):
        for j in range(i):
            arr[i][j], arr[j][i] =  arr[j][i], arr[i][j]


    # Reverse elements in each row
    for i in range(n):
        j = 0
        k = m-1
        while j < k:
            arr[i][j],arr[i][k] = arr[i][k], arr[i][j]
            j+=1 
            k-=1
    
    for i in range(n):
        print(arr[i])


def two_sum_brute(nums,target):
    """
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    arr_len = len(nums)

    for i in range(arr_len):
        for j in range(i+1, arr_len):
            if nums[i] + nums[j] == target:
                return [i,j]
    return -1

def two_sum_better_hashing(nums,target):
    """
    
    Time Complexity: O(N logN) or O(N^2) [Worest case if all the elements are colliding in hash]
    Space Complexity: O(N)
    """
    h_arr = dict()

    for i in range(len(nums)):
        diff = target - nums[i]
        print(h_arr)
        if diff in h_arr:
            return [h_arr.get(diff), i]
        else:
            h_arr[nums[i]] = i
    
    return -1


def two_sum_slightly_optimal(nums, target):
    """
    Optimal just to return whether the two sum exists or not. To return the indexes, we need to 
    use some other data struct to store the indexes.

    First sort the arr and use two pointer approach to search for the elements.

   Time Complexity: O(N) + O(N*logN), where N is size of the array. As the loop will run at most N times & sorting the array will take N * logN time complexity
   Space Complexity: O(N), because of the external data structure created to store the array elements along with their indices
    """
    nums = [[nums[i],i] for i in range(len(nums))]

    nums.sort(key=lambda x:x[0])

    i = 0
    j = len(nums)-1

    while i < j:
        sum = nums[i][0] + nums[j][0]
        if sum == target:
            return [nums[i][1] , nums[j][1]]
        elif sum > target:
            j -= 1
        else:
            i+=1 
    return -1



# r = int(input())
# c = int(input())

k = int(input())

nums = [int(n) for n in input().split()]


# n = [[1,2,3], [4,5,6], [7,8,9]]

print(two_sum_slightly_optimal(nums,k))


