"""
Runtime: 44 ms, faster than 99.60% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 97.63% of Python3 online submissions for Palindrome Number.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
        
