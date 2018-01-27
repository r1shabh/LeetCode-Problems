__author__ = 'rishabh anand'


answers = ["1"]


class Solution(object):
    def countAndSay(self, n):
        global answers
        l = len(answers)
        while l < n:
            answers.append(self.helper(answers[l - 1]))
            l += 1
        return answers[n - 1]

    def helper(self, num):
        output = ""
        l = len(num)
        i = 1
        digit = num[0]
        occurences = 1
        while i < l:
            if num[i] == digit:
                occurences += 1
            else:
                output += str(occurences)
                output += str(digit)
                digit = num[i]
                occurences = 1
            i += 1
        output += str(occurences)
        output += str(digit)
        return output


s = Solution()
print s.countAndSay(1)
print s.countAndSay(8)
print answers
