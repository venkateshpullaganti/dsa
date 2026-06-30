
def find_lower_bound(nums, x, low, high, lower_bound):
    """
    Follow binary search and then update the lower bound only when ele >= current.
    Move to left if ele >= x else move to right.  
    Time: O(log2 N) 
    Space: O(1)
    """
    if low > high:
        return lower_bound

    mid = (low+high)//2
    if nums[mid] >= x:
        lower_bound = mid
        return find_lower_bound(nums, x, low, mid-1, lower_bound)
    else:
        return find_lower_bound(nums, x, mid+1, high, lower_bound)



# ------------- loop

class Solution:
    # Function to find the lower bound
    def lowerBound(self, nums, x):
        n = len(nums)
        for i in range(n):
            # Check the condition for 
            # the current element
            if nums[i] >= x:
                # If lower bound is found
                return i
        # If lower bound of 
        # target is not found
        return n

if __name__ == "__main__":
    arr = [1, 2, 2, 3]
    x = 2

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to find the lower bound
    ind = sol.lowerBound(arr,  x)

    print("The lower bound is the index:", ind)