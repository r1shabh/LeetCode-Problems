__author__ = 'rishabh anand'


class Solution(object):
    def isValid(self, s):
        s.replace(" ", "")
        parentheses = {")": "(", "]": "[", "}": "{"}
        myOpenStack = []
        for p in s:
            if p == "(" or p == "{" or p == "[":
                myOpenStack.append(p)
            else:
                if len(myOpenStack) == 0:
                    return False
                if parentheses[p] == myOpenStack[-1]:
                    myOpenStack.pop()
                else:
                    return False
        return len(myOpenStack) == 0
        """
        :type s: str
        :rtype: bool
        """


s = Solution()
print s.isValid("{}(")
print s.isValid("()[]{}")
print s.isValid("(]")
print s.isValid("([)]")
print s.isValid("([][]{})")
