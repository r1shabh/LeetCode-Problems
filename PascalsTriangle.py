__author__ = 'rishabh anand'


triangle = [[1], [1, 1]]

class Solution(object):
    def generate(self, numRows):
        global triangle
        if numRows <= len(triangle):
            return triangle[:numRows]
        self.load(numRows)
        return triangle[:numRows]
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

    def load(self, numRows):
        global triangle
        start = len(triangle)
        while start < numRows:
            l = [1]
            for i in range(1, len(triangle[-1])):
                l.append(triangle[-1][i] + triangle[-1][i - 1])
            l.append(1)
            triangle.append(l[:])
            start += 1
        l = [1]
        for i in range(1, len(triangle[-1])):
            l.append(triangle[-1][i] + triangle[-1][i - 1])
        l.append(1)
        triangle.append(l[:])


s = Solution()
print s.generate(1)
print s.generate(2)
print s.generate(3)
print s.generate(5)
