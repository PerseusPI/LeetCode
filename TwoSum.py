#LeetCode challenge TwoSum
def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):     
        for j in range(len(nums) - 1):
            if nums[i] + nums[j+1] == target:                  
                if j+1 != i:  
                    return [i, j+1]
