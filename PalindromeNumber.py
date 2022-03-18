"""
Runtime: 77 ms, faster than 68.32% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 34.22% of Python3 online submissions for Palindrome Number.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
        
