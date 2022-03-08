"""
Hard Challenge:
Runtime: 96 ms, faster than 87.71% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.3 MB, less than 52.56% of Python3 online submissions for Median of Two Sorted Arrays.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = [int(i) for i in nums1] + [int(i) for i in nums2]
        l.sort()
        if len(l) % 2 == 0:
            return float((l[int((len(l)/2))] + l[int((len(l)/2)) - 1]) / 2)
        return float(l[int((len(l)/2))])
