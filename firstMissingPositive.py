__author__ = 'rishabh anand'


def firstMissingPositive(nums):
    i = 0
    while i < len(nums):
        if nums[i] <= 0:
            nums.remove(nums[i])
        else:
            i += 1
    size = len(nums)
    for x in range(size):
        if 0 <= abs(nums[x]) - 1 < size:
            nums[abs(nums[x]) - 1] = -abs(nums[abs(nums[x]) - 1])
    for y in range(size):
        if nums[y] > 0:
            return y + 1
    return size + 1


print firstMissingPositive([1, 2, 0])
print firstMissingPositive([1, 1])
print firstMissingPositive([2, 3, 1])
