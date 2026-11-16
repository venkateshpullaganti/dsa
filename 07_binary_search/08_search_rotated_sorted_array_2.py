"""
class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):
        n = len(nums)
        low = 0
        high = n-1

        while low <=high:
            mid = (low+high)//2

            if nums[mid] == k:
                return True
            
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            
            if nums[low] <= nums[mid]:
                if nums[low] <= k <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
"""

# NOTE:  While checking the sorted array, use <= instead of only <

class Solution:
    # Function to search for the target element
    # in a rotated sorted array with duplicates
    def searchInARotatedSortedArrayII(self, arr, target):
        """
        Time Complexity: O(logN) for the best and average cases. As in the best and average scenarios, the binary search algorithm is primarily used and hence the time complexity is O(logN).
        However, in the worst-case scenario, it'll be O(N/2) where all array elements are the same but not the target (e.g., given array = {3, 3, 3, 3, 3, 3, 3}), we continue to reduce the search space by adjusting the low and high pointers until they intersect, 
        which will end up taking O(N/2) time complexity.

        Space Complexity:O(1), as we are not using any extra space to solve this problem.
        """
        n = len(arr)
        low, high = 0, n - 1
        
        # Applying binary search algorithm 
        while low <= high:
            mid = (low + high) // 2

            # Check if mid points to the target
            if arr[mid] == target:
                return True

            # Handle duplicates: if arr[low], arr[mid], and arr[high] are equal
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue

            # Check if the left part is sorted
            if arr[low] <= arr[mid]:
                # Eliminate the right part if target exists in the left sorted part
                if arr[low] <= target <= arr[mid]:
                    high = mid - 1
                # Otherwise eliminate the left part
                else:
                    low = mid + 1
            else:
                # If the right part is sorted and target exists in the right sorted part, eliminate the left part
                if arr[mid] <= target <= arr[high]:
                    low = mid + 1
                # Otherwise eliminate the right part
                else:
                    high = mid - 1
        
        # If target is not found
        return False

if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    target = 3 

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to search for the target element
    result = sol.searchInARotatedSortedArrayII(arr, target)

    if not result:
        print("Target is not present.")
    else:
        print("Target is present in the array.")