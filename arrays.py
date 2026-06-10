
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

# keep on comparing with nums[i] and if greater then place it at i+1 and increment i 
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




    FUNCTION majorityElement(nums):

    ── Phase 1: Find Candidate ──────────────────────────
    candidate ← 0
    count     ← 0

    FOR each num in nums:
        IF count == 0:
            candidate ← num        // reset candidate
            count     ← 1
        ELSE IF num == candidate:
            count ← count + 1      // reinforce candidate
        ELSE:
            count ← count - 1      // cancel out one occurrence

    ── Phase 2: Verify Candidate ────────────────────────
    freq ← 0

    FOR each num in nums:
        IF num == candidate:
            freq ← freq + 1

    IF freq > len(nums) / 2:
        RETURN candidate           // confirmed majority

    RETURN -1                      // no majority element exists


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


# ------------------ Majority Element 2 --------------------

def majority_ele_2_brute(nums):
    """
    Iterate over each element, count them and add

    Time Complexity: O(N^2)
    Space Complexity: O(1)
    
    """
    ans = []
    n = len(nums)

    for i in range(len(nums)):
        count = 0
        if len(ans) == 0 or ans[0] != nums[i]:
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count+=1
                
            if count > n//3:
               ans.append((nums[i]))

            if len(ans) > 1:
                break

    return ans

def majority_ele_2_better(nums):
    """
    Hash the each elements count.
    Compare the count > n//3 and return those elements.

    Time complexity: O(N)
    Space complexity: O(N)
    
    """
    ans = dict()

    n = len(nums)

    for i in range(n):
        ans[nums[i]] = ans[nums[i]] + 1 if ans.get(nums[i]) else 1
    
    eles = []
    for key,value in ans.items():
        if value > n//3:
            eles.append(key)
    return eles


def majority_ele_2_optimal_moors_voting(nums):
    """
    Moor voting algo but we take two vars and make sure 
    they are not same when making initializing each var.

    Time complexity: O(N)
    Space complexity: O(1) 

    FUNCTION majorityElementTwo(nums):

    ── Phase 1: Find Two Candidates ─────────────────────
    candidate1 ← None,  count1 ← 0
    candidate2 ← None,  count2 ← 0

    FOR each num in nums:

        IF count1 == 0 AND num ≠ candidate2:
            candidate1 ← num          // claim first empty slot
            count1     ← 1

        ELSE IF count2 == 0 AND num ≠ candidate1:
            candidate2 ← num          // claim second empty slot
            count2     ← 1

        ELSE IF num == candidate1:
            count1 ← count1 + 1       // reinforce candidate1

        ELSE IF num == candidate2:
            count2 ← count2 + 1       // reinforce candidate2

        ELSE:
            count1 ← count1 - 1       // cancel one of each
            count2 ← count2 - 1       //   against this intruder

    ── Phase 2: Verify Both Candidates ──────────────────
    count1 ← 0
    count2 ← 0

    FOR each num in nums:
        IF num == candidate1:  count1 ← count1 + 1
        IF num == candidate2:  count2 ← count2 + 1

    ── Phase 3: Collect Results ──────────────────────────
    result ← []

    IF count1 > floor(n / 3):  result.append(candidate1)
    IF count2 > floor(n / 3):  result.append(candidate2)

    RETURN result

    """
    count1 = 0
    ele1 = None

    count2 = 0
    ele2 = None

    n = len(nums)

    for i in range(n):
        if count1 == 0 and nums[i] != ele2:
            count1 = 1
            ele1 = nums[i]
        elif count2 == 0 and nums[i] != ele1:
            count2 = 1
            ele2 = nums[i]
        elif ele1 == nums[i]:
            count1+=1
        elif ele2 == nums[i]:
            count2+=1
        else:
            count1 -= 1
            count2 -= 1
    

    count1 = 0
    count2 = 0
    for i in range(n):
        if nums[i] == ele1:
            count1+=1
        elif nums[i] == ele2:
            count2+=1 
    
    ans = []
    if count1 > n//3:
        ans.append(ele1)
    
    if count2 > n//3:
        ans.append(ele2)
    
    return ans


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
    Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.

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



def three_sum_brute(nums):
    """
    Time Complexity: O(N2 x log(no. of unique triplets)), where N is size of the array.
    Inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. However, we are not considering the time complexity of sorting, as we are only sorting 3 elements each time.
    Note: For Java (HashSet), insertion operation takes O(1) time. Thus, the overall time complexity for Java code will be O(N2)

    Space Complexity: O(2 x no. of the unique triplets) + O(N) for using a set data structure and a list to store the triplets and extra O(N) for storing the array elements in another set.
    """
    tl = dict()

    num_len = len(nums)

    for i  in range(num_len):
        for j in range(i+1, num_len):
            for k in range(j+1,num_len):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets = [nums[i] , nums[j] , nums[k]]
                    triplets.sort()
                    tl[tuple(triplets)] = True

    ans =  [k for k in tl.keys()]
    return ans


def three_sum_better(nums):
    """
    Time Complexity: O(N2 x log(no. of unique triplets)), where N is size of the array.
    Inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. However, we are not considering the time complexity of sorting, as we are only sorting 3 elements each time.
    Note: For Java (HashSet), insertion operation takes O(1) time. Thus, the overall time complexity for Java code will be O(N2)

    Space Complexity: O(2 x no. of the unique triplets) + O(N) for using a set data structure and a list to store the triplets and extra O(N) for storing the array elements in another dict.
    """
    num_len = len(nums)

    if num_len < 3:
        return []
    
    tl_set = set()

    for i in range(num_len):
        hash_arr = dict()
        for j in range(i+1, num_len):
            diff = -(nums[i] + nums[j])
            if hash_arr.get(diff):
                triplets = [nums[i] , nums[j], diff]
                triplets.sort()
                tl_set.add(tuple(triplets))
            
            hash_arr[nums[j]] = True

    ans = [list(t) for t in tl_set]

    return ans

def three_sum_optimal_2pointer(nums):
    """
    Time Complexity: O(N3), where N is the size of the given array.
    Sorting the array takes O(NlogN) time, and the 3 nested loops take O(N3) time. Thus, the overall time complexity is O(N3) + O(NlogN), which boils down to O(N3).

    Space Complexity: O(no. of quadruplets), this space is only used to store the answer. No extra space is used to solve this problem. So, from that perspective, space complexity can be written as O(1).
    """
    num_len = len(nums)
    tls = []

    if num_len < 3:
        return []
    
    nums.sort()
    
    for i in range(num_len):
        if i > 0 and nums[i-1] == nums[i]:
            continue

        j = i+1
        k = num_len-1
        while j < k:

            summ = nums[i] + nums[j]+ nums[k]
            if summ == 0:
                tls.append([nums[i] , nums[j], nums[k]])
                j+=1
                k-=1

                while j < k and nums[j] == nums[j-1]:
                    j+=1
                while j < k and nums[k] == nums[k+1]:
                    k-=1
            elif summ < 0:
                j+=1
            else:
                k-=1

    return tls


def four_sum_brute(nums,target):
    """
    Time complexity : O(N4)
    Space complexity : O(No. of quads)

    """
    num_len = len(nums)
    if num_len < 4: 
        return []

    quads = set()

    for i in range(num_len):
        for j in range(i+1, num_len):
            for k in range(j+1, num_len):
                for l in range(k+1, num_len):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        quads.add(tuple(temp))

    return list(quads)


def four_sum_better(nums, target):
    num_len = len(nums)
    if num_len < 4: 
        return []

    quads = set()

    for i in range(num_len):
        for j in range(i+1, num_len):
            hash_nums = dict()
            for k in range(j+1, num_len):
                diff = target - (nums[i] + nums[j] + nums[k])
                if hash_nums.get(diff):
                    temp = [nums[i], nums[j], nums[k], diff]
                    temp.sort()
                    quads.add(tuple(temp))
                hash_nums[nums[k]] = True

    quads_list = [list(q) for q in quads]
    return quads_list


def four_sum_optimal_2pointer(nums, target):
    num_len = len(nums)
    if num_len < 4: 
        return []
    
    nums.sort()
    quads = []
    for i in range(num_len):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, num_len):

            if j > i+1 and nums[j] == nums[j-1]:
                continue

            l = j + 1
            m = num_len - 1
            while l < m:
                summ = nums[i]+  nums[j]+ nums[l] + nums[m]
                if summ == target:
                    quads.append([nums[i], nums[j],nums[l],nums[m]])
                    l+=1
                    m-=1
                    
                    while l < m and nums[l] == nums[l-1]:
                        l+=1
                    while l < m and nums[m] == nums[m+1]:
                        m-=1
                elif summ > target:
                    m-=1
                else:
                    l+=1

    return quads



#--------------------------- Sort array of 0,1 and 2s ------------------------------

def sort_012s_brute(nums):
    """
    Sort the array.
    Time complexity: O(N logN) : We use merge sort
    Space complexity: O(N)
    
    """
    nums.sort(key=lambda x:x[0])

    return nums


def sort_012s_better(nums):
    """
    Count the 0s, 1s and 2s and then populate the array again.

    Time complexity: O(N) + O(N) -> for counting and populating
    Space complexity: O(1)
    """

    count0= 0
    count1= 0
    count2 = 0

    for num in nums:
        if num == 0:
            count0 +=1 
        elif num == 1:
            count1 +=1 
        else:
            count2 += 1

    i = 0
    while i <= count0:
        nums[i] = 0
        i+=1

    for j in range(count1):
        nums[i] = 1
        i+=1

    for j in range(count2):
        nums[i] = 2
        i+=1

    return nums




def sort_012s_optimal_dutch_national_flag(nums):
    """
    have three pointers, low mid and high
    
    assume everything between 0 -> low-1,  low -> mid-1 and hight+1  -> end is sorted. 

    the mid -> high is not sorted. We start with this and keep moving from mid to high
    sorting everything.
    
    Time complexity: O(N) 
    Space complexity: O(1)
    """

    low = 0
    mid = 0
    high = len(nums)-1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid +=1 
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums




#--------------------------- Maximum sub array elements ------------------------------

def maximum_subarray_brute(nums):
    """
    Create all the possible sub arrays and sum them. 

    Time Complexity = ~ O(N^3), 3 nested loops (i,j & k). Nearly N^3 because the j & k loops 
    don't run till len of arr.

    Space Complexity: O(1), no extra space
    """
    max = float('-inf')

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            s = 0
            # sub_array=[]
            for k in range(i,j+1):
                s = s+nums[k]
                # sub_array.append(nums[k])
            # print(sub_array ,  s)
            if s > max:
                max = s

    return max


def maximum_subarray_better(nums):
    """
    Instead of creating all the sub arrays and adding them, we add the elements in
    the second loop itself with previous sum, avoiding 3rd nested loop.

    Time Complexity: ~O(N^2), for i and jth loops.
    Space Complexity: O(1), no extra space.
    
    """
    max = float('-inf')

    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
        s = 0
        # sub_arr = []
        for j in range(i, len(nums)):
            # sub_arr.append(nums[j])
            s = s+nums[j]
            if s > max:
                max = s
            # print(sub_arr)
    return max


def maximum_subarray_optimal_kadanes_algo(nums):
    """
    for max and sum vars,
    We will start by adding each num to sum, 
        we will update sum if sum > max, 
        we will reset sum to 0, when it goes below 0, so that we will always carry + num
    
    Time Complexity: O(N), we are iterating only once
    Space Complexity: O(1), no extra space
    
    """

    max = float('-inf')
    summ = 0

    arr_start = -1
    arr_end = -1

    start = 0

    for i in range(len(nums)):
       
        if summ == 0:
            start = i
            
        summ += nums[i]
        
        if summ > max:
            max = summ
            arr_start = start
            arr_end = i
        
        if summ < 0:
            summ = 0

    sub_arr = [nums[i] for i in range(arr_start, arr_end+1)]
    print(sub_arr)

    return (max, arr_start, arr_end)


# -------------------- Next permutation --------------------------

def next_permutation_optimal(nums):
    pivot_ind = -1
    l = len(nums)

    for i in range(l-1, -1, -1):
        if nums[i] > nums[i-1]:
            pivot_ind = i-1
            break
    
    if pivot_ind == -1:
        nums.reverse()
        return nums
    
    for i in range(l-1, pivot_ind, -1):
        if nums[i] > nums[pivot_ind]:
            nums[i], nums[pivot_ind] = nums[pivot_ind], nums[i]
            break

    nums[pivot_ind+1:] = reversed(nums[pivot_ind+1:])

    return nums
    

# ------------------ Repeating and missing number ---------------------

def repeating_and_missing_num_brute(nums):
    """
    Nested loop to count the nums and break when you got the both nums

    Time Complexity: O(N^2), nested loops
    Space Complexity: O(1), No extra space
    
    """
    repeating_num = -1
    missing_num = -1

    for i in range(1, len(nums)+1):
        count = 0
        for j in range(len(nums)):
            if i == nums[j]:
                count+=1
            if count > 1:
                repeating_num = i
                break
        if count == 0:
            missing_num = i
        
        if repeating_num != -1 and missing_num != -1:
            break
    
    return [repeating_num, missing_num]


def repeating_and_missing_num_better_hashing(nums):
    n = len(nums)
    num_hash = [0 for i in range(n+1)]

    for i in range(len(nums)):
        num_hash[nums[i]] += 1
    
    ans = [-1,-1]

    for i in range(n+1):
        if num_hash[i] > 1:
            ans[0] = i
        elif num_hash[i] == 0:
            ans[1] = i

    return ans 

def repeating_and_missing_num_optimal(nums):
    """
    Using equations:
    (sum of elements) - (sum of first n natural nums) -> x - y = v1
    (sum of squares of elements) - (sum of squares of n natural nums) -> x^2 - y^2 = v2

    x^2 - y^2 = v2 -> (x+y) (x-y) = v2

    x-y = v1
    (x+y) (x-y) = v2

    (x+y) = v2/(x-y)

    x+y = v2/v1
    x-y = v1

    Time Complexity: O(N), for sum & pow
    Space complexity: O(1), no extra
    
    """
    n = len(nums)

    sN = (n*(n+1))//2
    s2N =( (n*(n+1)) * (2*n+1))//6

    s = 0
    s2 = 0

    for num in nums:
        s += num
        s2 += num * num
    
    # x-y = v1
    x_sub_y = s - sN 

    # x^2 - y^2 = v2
    pow_diff = s2 - s2N
    x_add_y = pow_diff//x_sub_y  # x+y

    x =(x_add_y+x_sub_y)//2

    y = x_add_y-x

    return [x,y]


# --------------------- Count Inversions ----------------------------------------

def count_inversions_brute(nums):
    """
    Iterate nums and check with the elements that are left to it. 

    Time : O(N^2) , nested loops
    Space: O(1)
    
    """
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                count+=1

    return count



def merge_and_count_reverse_pairs(nums, low, mid, high, count):
    left = low
    right = mid+1

    temp = []

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            count += mid-left+1
            right+=1

    while left <= mid:
        temp.append(nums[left])
        left+=1
    
    while right <= high:
        temp.append(nums[right])
        right+=1
    
    for i in range(low, high+1):
        nums[i] = temp[i-low]
    
    return count


def count_inversions_optimal_merge_sort(nums,low, high):
    count = 0
    if low < high:
        mid = (low+high)//2

        count+= count_inversions_optimal_merge_sort(nums, low, mid)
        count+= count_inversions_optimal_merge_sort(nums, mid+1, high)
        count+= merge_and_count_reverse_pairs(nums, low, mid, high)

        return count
    return count


# ------------------------------Reverse Pairs :  Count of pairs 2x -------------------------
"""
Find the pairs in the arr such that a[i] > 2 * a[j] and i < j.

"""

def reverse_pairs_2x_brute(nums):
    """
        Iterate over the nums and find the pairs and count them.
        Time : O(N^2)
        Space: O(1)
    """

    count = 0
    n = len(nums)
    if n < 2:
        return count

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > 2 * nums[j]:
                count+=1 
    return count



def merge_sort_arr_reverse_pairs(nums, low, mid, high):
    right = mid+1
    left = low
    temp = []

    while left <= mid and right <=high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    
    while left <= mid:
        temp.append(nums[left])
        left+=1

    while right <= high:
        temp.append(nums[right])
        right+=1
    
    
    for i in range(low, high+1):
        nums[i] = temp[i-low]
    
    return nums

def count_pairs_2x(nums, low, mid, high):
    count = 0

    right = mid+1

    for i in range(low, mid+1):
        while right <= high and nums[i] > 2 * nums[right]:
            right+=1
        count += right - (mid+1)
    print(f"Final iteration count {nums[low]} -> {nums[high]} : {count}")
    return count


def merge_and_count_reverse_pairs(nums, low, high):

    count = 0
    if low >= high:
        return count
    
    mid = (low+high)//2

    count += merge_and_count_reverse_pairs(nums, low, mid)
    count += merge_and_count_reverse_pairs(nums, mid+1, high)
    count += count_pairs_2x(nums, low, mid, high)
    merge_sort_arr_reverse_pairs(nums, low, mid, high)

    return count


def reverse_pairs_2x_optimal_merge_sort(nums):
    n = len(nums)
    return merge_and_count_reverse_pairs(nums, 0, n-1)




# ----------------------- Max Product subArray ------------------

def max_product_brute(nums):
    """
    Find all the sub arrays and product of those and compare.
    Return the max.

    Time : ~O(N^3), 3 nested loops
    Space : O(1)

    """
    n= len(nums)
    max_product = float('-inf')

    for i in range(0, n):
        for j in range(i, n):
            product = 1
            for k in range(i, j+1):
                product = product * nums[k]
            if product > max_product:
                max_product = product
    return max_product       


def max_product_better(nums):
    """
    We dont create the sub arrays, the sub array element we get from i -> j loop.
    Ex: [4,0,2,3,0]
        i     j  prod
        0 -> 0 : 4
        0 -> 1 : 4 * 0
        0 -> 2 : 4 * 0 * 2
        0 -> 3 :  4 * 0 * 2 *  3
        0 -> 4 : 4 * 0 * 2 * 3 * 0

        similarly with i = 1, 2, 3, 4

    Time:  O(N^2)
    Space: O(1)
    """
    n = len(nums)
    max_product = float("-inf")
    
    for i in range(0,n):
        product = 1
        if nums[i] > max_product:
            max_product = nums[i]

        for j in range(i, n):
            product = product * nums[j]
            if product > max_product:
                max_product = product
                # sub array is i -> j
    
    return max_product

def max_product_optimal(nums):
    pass


# r = int(input())
# c = int(input())

# k = int(input())

nums = [int(n.strip()) for n in input().split(",")]

# n = [[1,2,3], [4,5,6], [7,8,9]]

n = len(nums)
print(max_product_better(nums))




