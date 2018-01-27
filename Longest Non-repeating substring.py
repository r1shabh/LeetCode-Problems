__author__ = 'rishabh anand'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxHere = [0] * n
        maxLen = 0
        output = ""
        for i in range(n):
            if s[i] in output:
                output = s[i]
                maxHere[i] = 1
            else:
                output += s[i]
                maxHere[i] = 1 + maxHere[i - 1]
            maxLen = max(maxLen, maxHere[i])
        print maxHere
        return maxLen

    def lengthOfLongestSubstring1(self, s):
        output = ""
        n = len(s)
        temp = ""
        for i in range(n):
            if len(temp) == 0:
                temp += s[i]
            else:
                if s[i] == temp[-1]:
                    if len(temp) > len(output):
                        output = temp
                    temp = ""
                    temp += s[i]
                else:
                    temp += s[i]
        if len(temp) > len(output):
            return temp
        return output
    """
    :type s: str
    :rtype: int
    """


s = Solution()
print s.lengthOfLongestSubstring("bbbbbb")
print s.lengthOfLongestSubstring("abcabcbb")
print s.lengthOfLongestSubstring("dvdf")
