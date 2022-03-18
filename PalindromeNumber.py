class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        debut = 0
        fin = len(x)-1
        while debut <= fin:
            if x[debut] != x[fin]:
                return False
            debut+=1
            fin-=1
        return True
            
        
        
