__author__ = 'rishabh anand'


class Solution(object):
    def maxProfit(self, prices):
        output = 0
        n = len(prices)
        maxProfit = [0] * n
        pmin = prices[0]
        for i in range(n):
            if prices[i] < pmin:
                pmin = prices[i]
            if i > 0:
                if prices[i] > prices[i - 1]:
                    maxProfit[i] = prices[i] - pmin
                else:
                    maxProfit[i] = maxProfit[i - 1]
            output = max(output, maxProfit[i])
        return output


s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])
print s.maxProfit([7, 2, 5, 3, 6, 10])
print s.maxProfit([7, 6, 4, 3, 1])
