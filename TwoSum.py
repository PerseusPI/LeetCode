"""
Runtime: 5804 ms, faster than 12.24% of Python3 online submissions for Two Sum.
Memory Usage: 15.1 MB, less than 64.24% of Python3 online submissions for Two Sum.
"""

#LeetCode challenge TwoSum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):     
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:                   
                    return [i, j]
