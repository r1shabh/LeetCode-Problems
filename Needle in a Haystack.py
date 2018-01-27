__author__ = 'rishabh anand'


class Solution(object):
    def strStr(self, haystack, needle):
        h = len(haystack)
        n = len(needle)
        if n == h:
            if haystack == needle:
                return 0
            else:
                return -1
        if n > h:
            return -1
        i = 0
        while i < h:
            found = True
            temp = i
            for j in range(n):
                if temp >= h or haystack[temp] != needle[j]:
                    found = False
                temp += 1
            if found:
                return i
            i += 1
        return -1


s = Solution()
print s.strStr("hello", "ll")
print s.strStr("aaaaa", "bba")
print s.strStr("mississippi", "issi")
print s.strStr("", "")
