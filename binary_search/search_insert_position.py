
# ------ Brute Force ----------

class BruteSolution:
    def searchInsert(self, nums, target):
        """
        Iterate through the list and if you find any element >= target
        return that index, else return the len(nums)

        Time: O(N), iterating each element
        Space: O(1) 

        """
        # Iterate through the list
        for i in range(len(nums)):
            # If current element is greater than
           # or equal to the target
            if nums[i] >= target:
                # Return the current index
                return i
        # If target is greater than all elements, 
        # return the length of the list
        return len(nums)
    


class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        idx = n
        low = 0
        high = n-1

     # Applying Binary Search Algorithm
        while low <= high:
            mid = (low+high)//2

            # If mid element is greater than 
            # or equal to target, update ans 
            # and search the left half
            if nums[mid] >= target:
                idx = mid
                high = mid - 1
            else:
                # Otherwise, search the right half
                low = mid + 1
        return idx


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 8

    # Create an instance of the Solution class
    sol = Solution()

    # Find the insertion index
    ind = sol.searchInsert(nums, target)

    print("The index is:", ind)
