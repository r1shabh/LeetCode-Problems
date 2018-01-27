__author__ = 'rishabh anand'


class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums):
            if nums[i] > target:
                return i
            if nums[i] == target:
                return i
            i += 1
        return i
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


s = Solution()
print s.searchInsert([1, 3, 5, 6], 5)
print s.searchInsert([1, 3, 5, 6], 2)
print s.searchInsert([1, 3, 5, 6], 7)
print s.searchInsert([1, 3, 5, 6], 0)

