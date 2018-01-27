__author__ = 'rishabh anand'


class Solution(object):
    def maxProfit(self, prices):
        output = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                output += prices[i] - prices[i - 1]
        return output


s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])
print s.maxProfit([7, 2, 5, 3, 6, 10])
print s.maxProfit([7, 6, 4, 3, 1])
