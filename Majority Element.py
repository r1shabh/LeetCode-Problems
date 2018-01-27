__author__ = 'rishabh anand'


class Solution(object):
    def majorityElement(self, nums):
        output = nums[0]
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        maxFreq = freq[nums[0]]
        for key in freq:
            if maxFreq < freq[key]:
                output = key
                maxFreq = freq[key]
        return output


s = Solution()
print s.majorityElement([1, 1, 1, 2, 2, 2, 2])
