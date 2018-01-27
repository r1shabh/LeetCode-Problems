__author__ = 'rishabh anand'


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        n = len(intervals)
        output = []
        start = starts[0]
        end = ends[0]
        for i in range(n):
            try:
                if starts[i + 1] > ends[i]:
                    output.append(Interval(start, end))
                    start = starts[i + 1]
                end = ends[i + 1]
            except IndexError:
                output.append(Interval(start, end))
        return output
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """

def printIntervals(intervals):
    for i in intervals:
        print "[" + str(i.start) + ", " + str(i.end) + "]",
    print ""

s = Solution()
i1 = Interval(1, 3)
i2 = Interval(2, 6)
i3 = Interval(8, 10)
i4 = Interval(15, 18)
printIntervals([i1, i2, i3, i4])
printIntervals(s.merge([i1, i2, i3, i4]))
