__author__ = 'rishabh anand'


conversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(s):
    ans = 0
    i = 0
    if len(s) == 1:
        return conversion[s]
    while i < len(s) - 1:
        if conversion[s[i]] < conversion[s[i+1]]:
            ans -= conversion[s[i]]
            ans += conversion[s[i+1]]
            i += 2
        else:
            ans += conversion[s[i]]
            i += 1
        if i == len(s) - 1:
            ans += conversion[s[i]]
    return ans


print romanToInt("D")
