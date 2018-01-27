__author__ = 'rishabh anand'


import math


def isPalindrome(x):
        if x > 0:
            digits = int(math.log10(x)) + 1
        elif x == 0:
            digits = 1
        else:
            digits = int(math.log10(-x)) + 1
            x = -x
        if digits == 1:
            return True
        leftExp = digits
        rightExp = 1
        while leftExp > rightExp:
            if x % (10 ** leftExp) // (10 ** (leftExp-1)) != x % (10 ** rightExp) // (10 ** (rightExp - 1)):
                return False
            leftExp -= 1
            rightExp += 1
        return True

print(isPalindrome(1001))
