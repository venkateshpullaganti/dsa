"""
class Solution:
    def floorSqrt(self, n: int) -> int:
        if n <= 1:
            return n

        low = 1
        high = n

        while low <= high:
            mid = (low + high)//2

            if (mid * mid) <= n:
                low = mid + 1
            else:
                high = mid - 1
        
        return high  
        # Our value will be in high because when we start the low was at possible values and the high will be at not possible values
        # As we iterate eventually we cross low > high, where low will go to not possible and high will be at possible values at our ans point
"""


class Solution:
    """ 
    Complexity Analysis: 
        Time Complexity:O(logN), where N is the given number. We are basically using the Binary Search algorithm.

        Space Complexity: As no additional space is used, so the Space Complexity is O(1). 
     """
    def floorSqrt(self, n: int) -> int:
        low, high = 1, n
        
        # Binary search on the answer space
        while low <= high:
            mid = low + (high - low) // 2
            val = mid * mid  # Python ints are unbounded
            
            # Check if val is less than or equal to n
            if val <= n:
                # Move to the right part
                low = mid + 1
            else:
                # Move to the left part
                high = mid - 1
        
        # Return the floor of square root
        return high


def main():
    n = 28
    
    # Create an object of the Solution class
    sol = Solution()
    
    ans = sol.floorSqrt(n)
    
    # Print the result
    print(f"The floor of square root of {n} is: {ans}")


if __name__ == "__main__":
    main()
