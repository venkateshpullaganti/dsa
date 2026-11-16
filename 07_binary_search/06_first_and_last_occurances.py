class BinarySearchSolution:
    # Function to find the first occurrence of the target
    def firstOccurrence(self, nums, target):
        low, high = 0, len(nums) - 1
        first = -1

        # Applying Binary Search Algorithm
        while low <= high:
            mid = low + (high - low) // 2

            # If the target element is found, we 
            # update the first variable to mid and
            # eliminate the right half to look for 
            # more smaller index where target is present
            if nums[mid] == target:
                first = mid
                high = mid - 1

            # If middle element is smaller,
            # we eliminate the left half
            elif nums[mid] < target:
                low = mid + 1

            # If middle element is greater,
            # we eliminate the right half
            else:
                high = mid - 1

        return first

    # Function to find the last occurrence of the target
    def lastOccurrence(self, nums, target):
        low, high = 0, len(nums) - 1
        last = -1

        # Applying Binary Search Algorithm
        while low <= high:
            mid = low + (high - low) // 2

            # If the target element is found, we 
            # update the last variable to mid and
            # eliminate the left half to look for 
            # more greater index where target is present
            if nums[mid] == target:
                last = mid
                low = mid + 1

            # If middle element is smaller,
            # we eliminate the left half
            elif nums[mid] < target:
                low = mid + 1

            # If middle element is greater,
            # we eliminate the right half
            else:
                high = mid - 1

        return last

    # Function to find the first and last occurrences of the target
    def searchRange(self, nums, target):

        # Function call to find the first occurence of target
        first = self.firstOccurrence(nums, target)

        # If the target is not present in the array
        if first == -1:
            return [-1, -1]

        # Function call to find the last occurence of target
        last = self.lastOccurrence(nums, target)

        return [first, last]




class BoundsSolution:
    def searchRange(self, nums, target):

        def find_lower_bound(nums, target):
            low = 0 
            high = len(nums) - 1
            bound = len(nums)
            while low <= high:
                mid = (low+high)//2
                if nums[mid] >= target:
                    bound = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return bound
        
        def find_upper_bound(nums, target):
            low = 0 
            high = len(nums) - 1
            bound = len(nums)
            while low <= high:
                mid = (low+high)//2
                if nums[mid] > target:
                    bound = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return bound
        
        first_occ = find_lower_bound(nums, target)

        if first_occ == len(nums) or nums[first_occ] != target:
            return [-1,-1]
        last_occ = find_upper_bound(nums, target)
        return [first_occ, last_occ-1]



class LinearSolution:
    def searchRange(self, nums, target):
        first = -1
        last = -1
        for i in range(len(nums)):

            if nums[i] == target:
                if first == -1:
                    first = i
                    last = i
                else:
                    last = i
        return [first, last]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # Create an instance of the Solution class
    sol = BinarySearchSolution()

    # Function call to find the first and last occurrences
    result = sol.searchRange(nums, target)

    print("The first and last occurrences are at indices:", result[0], "and", result[1])