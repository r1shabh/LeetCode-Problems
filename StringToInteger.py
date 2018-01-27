__author__ = 'rishabh anand'


import string


def myAtoi(str):
    output = 0
    newstr = str.replace(" ", "")
    if newstr == "":
        return 0
    if newstr[0] == '-':
        length = len(newstr) - 1
        start = 1
        exp = length - 1
        while start <= length:
            output += int(newstr[start]) * (10 ** exp)
            start += 1
            exp -= 1
        output *= -1

    else:
        length = len(newstr)
        start = 0
        exp = length - 1
        while start < length:
            output += int(newstr[start]) * (10 ** exp)
            start += 1
            exp -= 1
    return output

print myAtoi("2147483648")
print string.atoi("-0012a42", 10)
