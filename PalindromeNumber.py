class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        g = ""
        for i in reversed(x):
            g += str(i)
        if str(g) == str(x):
            return True
        return False
