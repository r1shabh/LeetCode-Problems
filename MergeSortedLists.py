__author__ = 'rishabh anand'


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while len(nums1) > m:
            nums1.pop()
        i1 = 0
        i2 = 0
        while i1 < m and i2 < n:
            if nums2[i2] >= nums1[i1]:
                if i1 == m - 1 or nums1[i1 + 1] >= nums2[i2]:
                    nums1.insert(i1 + 1, nums2[i2])
                    i2 += 1
                    i1 += 1
                    m += 1
            else:
                nums1.insert(i1, nums2[i2])
                i2 += 1
                i1 -= 1
                m += 1
            i1 += 1
        while i2 < n:
            nums1.append(nums2[i2])
            i2 += 1
        print nums1
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """


s = Solution()
s.merge([1, 2, 3, 4], 4, [2, 3, 5], 3)
s.merge([1, 2], 2, [2, 3, 5], 3)
s.merge([2, 3, 5], 3, [1, 5], 2)
s.merge([4], 1, [1, 2, 3, 4, 5], 5)
s.merge([0], 0, [1], 1)
s.merge([1, 0], 1, [2], 1)
