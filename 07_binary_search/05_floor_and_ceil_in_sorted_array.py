class Solution:
    def getFloorAndCeil(self, nums, x):
        """
        Floor: The largest element that is <= x
        Ceil: The smallest element that is >= x
        """

        def find_floor(nums, x):
            """
            To find the largest element <= x, we need to check the condition <= x and then
            move to the right of the array for the largest -> low = mid + 1
            
            """
            n = len(nums)
            low = 0
            high = n-1
            ans = -1

            while low <= high:
                mid = (low+high)//2
                if nums[mid] <= x:
                    ans = nums[mid]
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        
        def find_ceil(nums,x):
            """
            To find the smallest element that is >= x, we need to check
            num >= x and then move the searching to left for the smallest, high = mid-1 
            """
            n = len(nums)
            low = 0
            high = n-1
            ans = -1
            
            while low <= high:
                mid = (low+high)//2
                if nums[mid] >= x:
                    ans = nums[mid]
                    high = mid -1
                else:
                    low = mid + 1
            return ans
        
        return [find_floor(nums, x), find_ceil(nums,x)]
       


if __name__ == "__main__":
    nums = [3, 4, 4, 7, 8, 10]
    x = 5

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to get floor and ceil
    result = sol.getFloorAndCeil(nums, x)

    print("The floor and ceil are:", result[0], result[1])
