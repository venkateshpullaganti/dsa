# class Solution:
#     def upperBound(self, nums, x):
#         bound = len(nums)

#         low = 0
#         high = len(nums)-1
#         while low <= high:
#             mid = (low+high)//2
#             if nums[mid] > x:
#                 bound = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return bound


class Solution:
    # Function to find the upper bound
    def upperBound(self, nums, x):
        low, high = 0, len(nums) - 1
        ans = len(nums)

        # Binary search to find the upper bound
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2

            # Update ans if current
            #  element is greater than x
            if nums[mid] > x:
                ans = mid
                high = mid - 1
            else:
                # Otherwise, move to the right half
                low = mid + 1

        return ans

if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    x = 2

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to find the upper bound
    ind = sol.upperBound(nums, x)

    print("The upper bound is the index:", ind)