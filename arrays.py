
# check is array is sorted
def isSorted(nums):
    is_sorted = True
    i = 0
    j = 1

    # while j <= len(nums)-1:
    #     if nums[i] > nums[j]:
    #         is_sorted = False
    #     i+=1
    #     j+=1
    # return is_sorted

    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            is_sorted = False
            break
    return is_sorted


def remove_dups(nums):
    num_set = set()
    for ele in nums:
        num_set.add(ele)
    i = 0 
    for ele in num_set:
        nums[i] = ele
        i+=1
    return nums

def remove_dups_optimized(nums):
    i = 0
    j = 1
    while j <= len(nums)-1:
        if nums[j] > nums[i]:
            nums[i+1] = nums[j]
            i += 1
        j +=1
    return i+1



nums = [int(n) for n in input().split()]

print(remove_dups_optimized(nums))