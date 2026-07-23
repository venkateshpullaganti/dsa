"""
class Solution:
    def can_we_place(self, nums, total_cows, distance):
        cows = 1
        last = nums[0]
        n = len(nums)

        for i in range(1,n):
            if nums[i] - last >= distance:
                cows+=1
                last = nums[i]
                if cows >= total_cows:
                    return True
            
        return False
        

    def aggressiveCows(self, nums, k):

        n = len(nums)
        nums.sort()

        low = 1
        high = nums[n-1] - nums[0]

        while low <= high:
            mid = (high + low)//2

            if self.can_we_place(nums, k, mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
"""


class Solution:
    """Function to check if we can place 'cows' 
    cows with at least 'dist' distance apart"""
    def canWePlace(self, nums, dist, cows):
        # Size of array
        n = len(nums)
        
        # Number of cows placed
        cntCows = 1
        
        # Position of last placed cow
        last = nums[0]
        for i in range(1, n):
            if nums[i] - last >= dist:
                # Place next cow
                cntCows += 1
                
                # Update the last location
                last = nums[i]
            if cntCows >= cows:
                return True
                
        return False

    """ Function to find the maximum possible minimum
    distance 'k' cows can have between them in 'nums'"""
    def aggressiveCows(self, nums, k):
        # Size of array
        n = len(nums)
        
        # Sort the nums
        nums.sort()
        
        low = 1
        high = nums[n - 1] - nums[0]
        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            if self.canWePlace(nums, mid, k):
                low = mid + 1
            else:
                high = mid - 1
        return high

if __name__ == "__main__":
    nums = [0, 3, 4, 7, 10, 9]
    k = 4
    
    # Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.aggressiveCows(nums, k)
    
    # Output the result
    print("The maximum possible minimum distance is:", ans)


"""
Complexity Analysis: 
Time Complexity:O(NlogN) + O(N *log(max-min)), where N is size of the array, max is the maximum element in array, min is the minimum element in array.
O(NlogN) for sorting the array. As binary search is applied, which runs for 1 to (max-min) to check all possible distances, so O(log(max-min)). Inside the loop, canWePlace() function is being called for each distance. Now, inside the canWePlace() function, the loop runs for N times.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

"""