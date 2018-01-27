__author__ = 'rishabh anand'


class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 1
        if n == 0:
            return 0
        num = nums[0]
        copies = 0
        while i < n:
            if nums[i] == num:
                copies += 1
                if copies == 2:
                    nums.pop(i)
                    n -= 1
                    copies -= 1
                else:
                    i += 1
            else:
                if i < n:
                    num = nums[i]
                i += 1
                copies = 0
        return n
        """
        :type nums: List[int]
        :rtype: int
        """


s = Solution()
nums = [1, 1, 1, 2, 3, 3]
print s.removeDuplicates(nums)
print nums
