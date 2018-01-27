__author__ = 'rishabh anand'


def twoSum(nums, target):
    for i in range(len(nums)):
        if target - nums[i] in nums:
            j = nums.index(target-nums[i])
            if i != j:
                return [i, j]
    return []

print twoSum([3, 5, 3], 6)

