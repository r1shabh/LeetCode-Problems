__author__ = 'rishabh anand'


class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        n = len(matrix[0])
        low = 0
        high = len(matrix) * n - 1
        x = low + (high - low) / 2
        while high - low >= 1:
            i = x / n
            j = x % n
            if high == low + 1:
                return target == matrix[low/n][low % n] or target == matrix[high/n][high % n]
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                low = x
            else:
                high = x
            x = low + (high - low) / 2
        return target == matrix[low/n][low % n] or target == matrix[high/n][high % n]
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


s = Solution()

print s.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3), True

print s.searchMatrix([[1, 3, 5],
                      [7, 10, 11],
                      [16, 20, 23],
                      [30, 34, 50]
                      ], 50), True

print s.searchMatrix([[1, 3, 5],
                      [7, 10, 11],
                      [16, 20, 23],
                      [30, 34, 50]
                      ], 8), False

print s.searchMatrix([[1, 2]], 2), True
print s.searchMatrix([[1, 1]], 2), False
print s.searchMatrix([], 0), False
print s.searchMatrix([[]], 0), False
print s.searchMatrix([[1]], 1)
print s.searchMatrix([[1], [3]], 3)

print s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 10), True
