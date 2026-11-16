# class Solution:
#     def countOccurrences(self, arr, target):
#         lower_bound = 0
#         upper_bound = 0
#         low, high = 0, len(arr)-1

#         if arr[0] == arr[high] == target:
#             return len(arr)

#         while low <= high: # < 0r <= ??
#             mid = (low+high)//2

#             if arr[mid] == target:
#                 lower_bound = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
        
#         low, high = 0, len(arr)-1

#         while low <= high:
#             mid = (low+high)//2

#             if arr[mid] > target:
#                 upper_bound = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
                
#         return upper_bound - lower_bound + 1


class Solution:
    def countOccurrences(self, arr, target):
        """
        A small modification of lower and upper bound. Find the first and last occurrence of 
        element and then return the index diffs.

        """
        first_occurrence = -1
        last_occurrence = -1
        low, high = 0, len(arr)-1

        if arr[0] == arr[high] == target:
            return len(arr)

        while low <= high: # < 0r <= ??
            mid = (low+high)//2

            if arr[mid] == target:
                first_occurrence = mid
                high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if first_occurrence == -1:
            return 0
        
        low, high = 0, len(arr)-1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == target:
                last_occurrence = mid
                low = mid + 1
            elif arr[mid] > target:
                high = mid-1
            else:
                low = mid + 1
                
        return last_occurrence - first_occurrence + 1

# Driver code
if __name__ == "__main__":
    # Create array
    arr = [1, 2, 2, 3, 2, 4]
    # Define target
    target = 2
    # Create solution object
    sol = Solution()
    # Call the function
    result = sol.countOccurrences(arr, target)
    # Print result
    print(result)