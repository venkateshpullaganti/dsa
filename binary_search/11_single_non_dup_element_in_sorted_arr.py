"""
class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        
        low = 1
        high = n-2

        while low <= high:
            mid = (low+high)//2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            is_even = mid%2 == 0
            if (is_even and nums[mid] == nums[mid+1]) or (not is_even and nums[mid] == nums[mid-1]):
                low = mid+1
            else:
                high = mid - 1
        
        return -1
"""


class Solution:
    """ Function to find the single non 
        duplicate element in a sorted array """
    def singleNonDuplicate(self, nums):
        n = len(nums) # Size of the array.

        # Edge cases:
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2

            # If nums[mid] is the single element:
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            # We are in the left part:
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                # Eliminate the left half:
                low = mid + 1
            # We are in the right part:
            else:
                # Eliminate the right half:
                high = mid - 1

        # Dummy return statement:
        return -1

nums = [1, 1, 2, 2, 3, 3, 4]

# Create an instance of the Solution class.
sol = Solution()

ans = sol.singleNonDuplicate(nums)

# Print the result.
print(f"The single element is: {ans}")




"""
Complexity Analysis: 
Time Complexity:O(logN), N is size of the given array. We are basically using the Binary Search algorithm.

Space Complexity: As no additional space is used, so the Space Complexity is O(1)
"""