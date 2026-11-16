"""
class Solution:
    def NthRoot(self, n, m):
        low = 1
        high = m

        while low <= high:
            mid = (low+high)//2
            val = mid ** n
            if val == m:
                return mid
            elif val > m:
                high = mid - 1
            else:
                low = mid + 1
        return -1
"""




class Solution:
    """
    Complexity Analysis:
        Time Complexity: O(logM * logN)
        The binary search on the search space (of size M) takes O(logM) and the helper function takes O(logN) taking overall O(logM * logN).

        Space Complexity: O(1), as there are only a couple of variables used.
    """


    # Helper function to check mid^N compared to M
    def helperFunc(self, mid, n, m):
        ans, base = 1, mid

        while n > 0:
            if n % 2 == 1:
                ans *= base
                if ans > m:
                    return 2  # Early exit
                n -= 1
            else:
                n //= 2
                base *= base
                if base > m:
                    return 2
        
        if ans == m:
            return 1
        return 0

    # Function to find the Nth root of M using Binary Search
    def NthRoot(self, N, M):
        low, high = 1, M
        
        while low <= high:
            mid = (low + high) // 2
            midN = self.helperFunc(mid, N, M)
            
            if midN == 1:
                return mid  # Found exact root
            elif midN == 0:
                low = mid + 1  # Move right
            else:
                high = mid - 1  # Move left
        
        return -1  # No integer root found

# Test case
n, m = 3, 27
sol = Solution()
ans = sol.NthRoot(n, m)
print("The answer is:", ans)
