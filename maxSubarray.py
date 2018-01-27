__author__ = 'rishabh anand'


class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        maxSums = []
        highest = nums[0]
        maxSums.append(highest)
        for i in range(1, n):
            maxSums.append(max(nums[i], maxSums[i - 1] + nums[i]))
            highest = max(highest, maxSums[i])
        return highest
        """
        :type nums: List[int]
        :rtype: int
        """


s = Solution()
print s.maxSubArray([-1, -2])
print s.maxSubArray([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
