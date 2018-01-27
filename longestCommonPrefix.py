__author__ = 'rishabh anand'


class Solution(object):
    def longestCommonPrefix(self, strs):
        lcp = ""
        i = 0
        while True:
            size = len(strs)
            for j in range(size):
                if j == 0:
                    if len(strs[j]) == i:
                        return lcp
                    lcp += strs[j][i]
                else:
                    if len(strs[j]) == i or lcp[i] != strs[j][i]:
                        return lcp[0:-1]
            if lcp == "":
                return lcp
            i += 1
        return strs[0]
        """
        :type strs: List[str]
        :rtype: str
        """


s = Solution()
print s.longestCommonPrefix(["", "asd"])
print s.longestCommonPrefix([])
print s.longestCommonPrefix(["qwerty", "qwerty", "qwerty", "qwerty"])
print s.longestCommonPrefix(["qwerty", "qwerty", "qwerty", "qwert"])
print s.longestCommonPrefix(["qwerty", "qwerty", "qrty", "qwerty"])
print s.longestCommonPrefix(["qwerty", "qwerty", "qwerty", "qwerty", ""])
print s.longestCommonPrefix(["qwerty", "qwerty", "qwerty", "qwertydfa"])