

"""
class Solution:
    def findMin(self, arr):
        low = 0
        high = len(arr) -1
        ans = float('inf')

        while low <= high:
            mid = (low+high)//2
            
            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    ans = arr[low]
                low = mid + 1
            else:
                if arr[mid] < ans:
                    ans = arr[mid]
                high = mid - 1
        return ans
"""


class Solution:
    """ Function to find minimum element
        in a rotated sorted array """
    def findMin(self, arr):
        # Initialize low and high indices
        low, high = 0, len(arr) - 1
        
        # Initialize ans to maximum integer value
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            
            # Check if left part is sorted
            if arr[low] <= arr[mid]:
                """ Update ans with minimum 
                    of ans and arr[low] """
                ans = min(ans, arr[low])
                
                # Move to the right part
                low = mid + 1
            else:
                """ Update ans with minimum 
                    of ans and arr[mid] """
                ans = min(ans, arr[mid])
                
                # Move to the left part
                high = mid - 1
        
        # Return the minimum element found
        return ans

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    
    #Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.findMin(arr)
    
    print("The minimum element is:", ans)
