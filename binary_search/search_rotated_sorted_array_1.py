class Solution:
    def search(self, nums, k):
        """
        
        """
        low = 0
        n = len(nums)
        high = n-1

       # Applying binary search algorithm
        while low <= high:
            mid = (low+high)//2 

             # Check if mid points to the target
            if nums[mid] == k:
                return mid 
            
            # Check if the left part is sorted
            if nums[low] <= nums[mid]:

                # Target exists in the left sorted part
                if nums[low] <= k <= nums[mid]:
                    high = mid-1
                else:
                # Target does not exist in the left sorted part
                    low = mid + 1
            else:
                # Check if the right part is sorted
                if nums[mid] <= k <= nums[high]:
                    # Target exists in the right sorted part
                    low = mid + 1
                else:
                    # Target does not exist in the right sorted part
                    high = mid - 1
        return -1
        


if __name__ == "__main__":
    nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    target = 1

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to search for the target element
    result = sol.search(nums, target)

    if result == -1:
        print("Target is not present.")
    else:
        print("The index is:", result)