__author__ = 'rishabh anand'


class Solution(object):
    def majorityElement(self, nums):
        output = []
        n = len(nums)
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for key in freq:
            if freq[key] > n/3:
                output.append(key)
        return output


s = Solution()
print s.majorityElement([1, 2, 1, 2])
print s.majorityElement([1, 1, 1, 4])
