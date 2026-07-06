class Solution:
    def search(self, nums, k):
        """
        
        """
        low = 0
        n = len(nums)
        high = n-1

        while low <= high:
            mid = (low+high)//2 
            if nums[mid] == k:
                return mid 
            if nums[low] <= nums[mid]:
                if nums[low] <= k <= nums[mid]:
                    high = mid-1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= k <= nums[high]:
                    low = mid + 1
                else:
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