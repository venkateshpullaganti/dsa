class SolutionBruteForce:
    def count_student(self, nums, pages):
        i = 0
        students = 0
        while i < len(nums):
            students += 1
            cnt = 0
            while i < len(nums) and cnt + nums[i] <= pages:
                cnt += nums[i]
                i+=1
        return students

    def findPages(self, nums, m):
        b = len(nums)

        if b < m:
            return -1

        low = max(nums)
        summ = sum(nums)

        for i in range(low, summ+1):
            cnt = self.count_student(nums, i)
            if cnt <= m:
                return i
        return low







class Solution:
    def count_student(self, nums, pages):
        i = 0
        students = 0
        while i < len(nums):
            students += 1
            cnt = 0
            while i < len(nums) and cnt + nums[i] <= pages:
                cnt += nums[i]
                i+=1
        return students

    def findPages(self, nums, m):
        n = len(nums)
        if n < m:
            return -1
        
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low+high)//2

            cnt = self.count_student(nums, mid)

            if cnt > m:
                low = mid + 1
            else:
                high = mid - 1
                
        return low

"""
Time Complexity:O(N * log(sum-max)), where N is size of the array, sum is the sum of all array elements, max is the maximum of all array elements.
As, binary search is being applied on [max, sum]. Inside the loop, we are calling the countStudents() function for the value of ‘mid’. Now, inside the countStudents() function, the loop runs for N times.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

"""