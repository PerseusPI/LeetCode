"""
Hard Challenge:
Runtime: 205 ms, faster than 8.72% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.2 MB, less than 52.56% of Python3 online submissions for Median of Two Sorted Arrays.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = [str(i) for i in nums1]
        nums2 = [str(i) for i in nums2]
        l = [int(i) for i in nums1]
        for i in nums2:
            l.append(int(i))
        l.sort()
        valeur = 0
        if len(l) % 2 == 0:
            valeur = l[int((len(l)/2))]
            valeur2 = l[int((len(l)/2)) - 1]
            return float((valeur + valeur2) / 2)
        valeur = l[int((len(l)/2))]
        return float(valeur)