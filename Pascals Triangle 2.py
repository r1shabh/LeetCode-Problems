__author__ = 'rishabh anand'


class Solution(object):
    def getRow(self, rowIndex):
        output = []
        for i in range(rowIndex + 1):
            output.append(self.choose(rowIndex, i))
        return output
        """
        :type rowIndex: int
        :rtype: List[int]
        """

    def factorial(self, n):
        return self.factorialHelper(n, 1)

    def factorialHelper(self, n, current):
        if n == 1 or n == 0:
            return current
        return self.factorialHelper(n - 1, current * n)

    def choose(self, n, m):
        return self.factorial(n) / (self.factorial(m) * self.factorial(n - m))

s = Solution()
print s.getRow(3)
print s.getRow(0)
print s.getRow(1)
print s.getRow(2)
print s.getRow(4)
