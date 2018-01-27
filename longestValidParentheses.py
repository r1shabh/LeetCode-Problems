__author__ = 'rishabh anand'


# noinspection PyUnreachableCode
class Solution(object):
    def longestValidParentheses(self, s):
        maxLength = [0] * len(s)
        output = 0
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    maxLength[i] = 2 + maxLength[i-2]
                else:
                    if i - maxLength[i - 1] > 0 and s[i - maxLength[i - 1] - 1] == "(":
                        maxLength[i] = maxLength[i-1] + maxLength[i - maxLength[i - 1] - 2] + 2
            output = max(output, maxLength[i])
        return output
        """
        :type s: str
        :rtype: int
        """
    '''
    def longestValidParentheses(self, s):
        length = 0
        maxLength = []
        count = 0
        for c in s:
            if c == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                if len(maxLength) == 0 or maxLength[-1] < length:
                    maxLength.append(length)
                length = 0
                count = 0
                maxLength.append(0)
            elif count == 0:
                length += 1
                if len(maxLength) == 0:
                    maxLength.append(length)
                else:
                    maxLength.append(maxLength[-1] + length)
                length = 0
            else:
                length += 1
        if len(maxLength) == 0 or length - count > maxLength[-1]:
            maxLength.append(length - count)
        return maxLength[-1]
        """
        :type s: str
        :rtype: int
        """
    '''

    '''
    version 1
    def longestValidParentheses(self, s):
        count = 0
        slist = []
        for c in s:
            slist.append(c)
        i = 0
        while i < len(slist):
            if slist[i] == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                slist.pop(i)
                count += 1
            else:
                i += 1
        return len(slist) - count
        """
        :type s: str
        :rtype: int
        """
    '''


solution = Solution()
'''
print solution.longestValidParentheses(")(")
print solution.longestValidParentheses("(()")
print solution.longestValidParentheses("()")
print solution.longestValidParentheses(")()())")
'''
print solution.longestValidParentheses("(()))())(")
print solution.longestValidParentheses("(()(((()")
print solution.longestValidParentheses("()(()))()()()()")
print solution.longestValidParentheses("()(())((()()()()")
print solution.longestValidParentheses("()(()")
print solution.longestValidParentheses("()(())")
