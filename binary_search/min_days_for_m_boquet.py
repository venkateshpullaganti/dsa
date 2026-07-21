"""
class Solution:
    def roseGarden(self, n, nums, k, m):
        n = len(nums)
        if n < k * m:
            return -1

        low = min(nums)
        high = max(nums)

        ans = -1

        while low <= high:
            mid = (low+high)//2

            boquet = 0
            cnt = 0
            for r in nums:
                if r <= mid:
                    cnt += 1
                else:
                    boquet += cnt//k
                    cnt = 0
            
            boquet+= cnt//k

            if boquet >= m:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
                
        return ans

"""



class Solution:
    """Function to check if it's possible to make
    m bouquets with k flowers each on day """
    def possible(self, nums, day, m, k):
        n = len(nums)
        
        # Count of flowers bloomed
        cnt = 0 
        
        # Count of bouquets formed
        noOfB = 0 

        # Count number of bouquets that can be formed
        for i in range(n):
            if nums[i] <= day:
                # Increment flower count
                cnt += 1 
            else:
                """ Calculate number of bouquets
                formed with flowers <= day """
                noOfB += (cnt // k)
                
                # Reset flower count
                cnt = 0 
        
        # Add remaining flowers as a bouquet
        noOfB += (cnt // k) 
        
        """ Return true if enough 
        bouquets can be formed """
        return noOfB >= m 

    """ Function to find the earliest day to
    make m bouquets of k flowers each """
    def roseGarden(self, n, nums, k, m):
        
        """ Calculate the minimum 
        number of flowers required """
        val = m * k 
        
        """ Impossible case: not enough 
            flowers to make m bouquets """
        if val > n:
            return -1 
        
        """ Find maximum and minimum
            bloom days in the array """
        mini = float('inf')
        maxi = float('-inf')
        for num in nums:
            mini = min(mini, num) 
            maxi = max(maxi, num) 
        
        """ Binary search to find the
            earliest day to make m bouquets """
        left = mini 
        right = maxi 
        ans = -1
        while left <= right:
            
            # Calculate the middle day
            mid = left + (right - left) // 2 
            
            """ Check if it's possible to 
                make m bouquets on day mid """
            if self.possible(nums, mid, m, k):
                
                # Update the answer to mid
                ans = mid 
                
                # Try for a smaller day
                right = mid - 1 
            else:
                left = mid + 1 
        
        """ Return the earliest day or 
        -1 if no such day exists"""
        return ans 

if __name__ == "__main__":
    arr = [7, 7, 7, 7, 13, 11, 12, 7] 
    
    n = len(arr)
    
    # Number of flowers per bouquet
    k = 3 
    
    # Number of bouquets needed
    m = 2 

    # Create an instance of the Solution class
    sol = Solution() 
    
    ans = sol.roseGarden(n, arr, k, m) 

    if ans == -1:
        print("We cannot make m bouquets.") 
    else:
        print(f"We can make bouquets on day {ans}") 
