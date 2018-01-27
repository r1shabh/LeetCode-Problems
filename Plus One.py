__author__ = 'rishabh anand'


class Solution(object):
    def plusOne(self, digits):
        x = [0] * (len(digits) - 1)
        x.append(1)
        output = []
        n = len(digits)
        carry = [0] * n
        for i in range(n - 1, -1, -1):
            temp = carry[i] + digits[i] + x[i]
            if i == 0:
                if temp >= 10:
                    output.insert(0, temp - 10)
                    output.insert(0, 1)
                else:
                    output.insert(0, temp)
            else:
                if temp >= 10:
                    output.insert(0, temp - 10)
                    carry[i - 1] = 1
                else:
                    output.insert(0, temp)
        return output
        """
        :type digits: List[int]
        :rtype: List[int]
        """

s = Solution()
print s.plusOne([1, 2, 3, 4])
print s.plusOne([9, 9, 9])
