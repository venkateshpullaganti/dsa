"""
class Solution:
    def findKRotation(self, nums):
        low = 0
        high = len(nums)-1
        idx = -1
        smallest = float('inf')

        while low <= high:

            mid = (low+high)//2

            if nums[low] <= nums[mid]:
                if nums[low] < smallest:
                    smallest = nums[low]
                    idx = low
                low = mid + 1
            else:
                if nums[mid] < smallest:
                    smallest = nums[mid]
                    idx = mid
                high = mid - 1
        return idx

"""



class Solution:
    """ Function to find the number of
        rotations in a rotated sorted array """
    def findKRotation(self, nums):
        low, high = 0, len(nums) - 1
        ans = float('inf')
        index = -1
        while low <= high:
            mid = (low + high) // 2
            
            """ Search space is already sorted
                then nums[low] will always be
                the minimum in that search space """
            if nums[low] <= nums[high]:
                if nums[low] < ans:
                    index = low
                    ans = nums[low]
                break
            
            # If left part is sorted update the ans
            if nums[low] <= nums[mid]:
                if nums[low] < ans:
                    index = low
                    ans = nums[low]
                # Eliminate left half
                low = mid + 1
            else:
                """ update the ans if it 
                    is less than nums[mid] """
                if nums[mid] < ans:
                    index = mid
                    ans = nums[mid]
                # Eliminate right half
                high = mid - 1
        
        # Return the index as answer
        return index

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    
    # Create an object of the Solution class
    sol = Solution()
    
    ans = sol.findKRotation(nums)
    
    # Print the result
    print(f"The array is rotated {ans} times.")
