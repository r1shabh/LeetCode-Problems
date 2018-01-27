__author__ = 'rishabh anand'

answers = [1, 1]

class Solution(object):
    def climbStairs(self, n):
        global answers
        if n < len(answers):
            return answers[n]
        self.addEntry(n)
        return answers[n]

    def addEntry(self, n):
        global answers
        start = len(answers)
        while start < n:
            answers.append(answers[-1] + answers[-2])
            start += 1
        answers.append(answers[-1] + answers[-2])

s = Solution()
print s.climbStairs(1)
print s.climbStairs(2)
print s.climbStairs(3)
print s.climbStairs(8)
