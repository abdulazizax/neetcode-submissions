class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 

        while l < r:
            if s[l] != s[r]:
                return (self.isPalidrome(s[l+1:r+1]) or self.isPalidrome(s[l:r]))

            l += 1
            r -= 1

        return True

        
    def isPalidrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True
        