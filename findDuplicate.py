__author__ = 'rishabh anand'


def findDuplicate(nums):
    nums.sort()
    print nums
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return 0


print findDuplicate([1, 2, 3, 2])
print findDuplicate([4, 1, 2, 3, 4])
print findDuplicate([3, 4, 1, 2, 5, 5, 6])
print findDuplicate([7, 9, 7, 4, 2, 8, 7, 7, 1, 5])