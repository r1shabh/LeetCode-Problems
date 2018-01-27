__author__ = 'rishabh anand'


def reverese(x):
    stringX = str(x)
    output = ''
    i = len(stringX) - 1
    end = 0
    if x < 0:
        output += '-'
        end += 1
    while i >= end:
        output += stringX[i]
        i -= 1
    return int(output)


print reverese(123)
print reverese(-123)
