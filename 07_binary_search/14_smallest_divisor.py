"""
class Solution:
    def get_div_sum(self, nums, d):
        s = 0

        for num in nums:
            s+= math.ceil(num/d)
        return s

    def smallestDivisor(self, nums, limit):
        n = len(nums)
        if n > limit:
            return -1
        
        low = 1
        high= max(nums)

        while low <= high:
            mid = (low+high)//2
        
            s = self.get_div_sum(nums, mid)
            
            if s <= limit:
                high = mid-1
            else:
                low = mid+1
        return low
"""


import math

class Solution:
    """ Helper function to find the 
    summation of division values"""
    def sumByD(self, nums, limit):
        # Size of array
        n = len(nums)  
        
        # Find the summation of division values
        sum_val = 0
        for num in nums:
            sum_val += math.ceil(num / limit)
        return sum_val

    # Function to find the smallest divisor
    def smallestDivisor(self, nums, limit):
        n = len(nums)
        if n > limit:
            return -1
        
        # Initialize binary search bounds
        low = 1
        high = max(nums)

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(nums, mid) <= limit:
                high = mid - 1
            else:
                low = mid + 1
        #Return the answer
        return low

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    limit = 8

    # Create an object of the Solution class
    sol = Solution()

    ans = sol.smallestDivisor(nums, limit)

    # Print the result
    print(f"The minimum divisor is: {ans}")



"""
Complexity Analysis: 
Time Complexity:O(log(max)*N), where max is the maximum element in the array, N is size of the array. We are applying binary search on our answers that are in the range of [1, max]. For every possible divisor ‘mid’, calling the sumByD() function. Inside that function, traversing the entire array, which results in O(N).

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

"""