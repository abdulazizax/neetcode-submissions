class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while r > l:
            if not self.isAlphanumeric(s[l]):
                l+=1
                continue

            if not self.isAlphanumeric(s[r]):
                r-=1
                continue 
        
            if s[l].lower() != s[r].lower():
                return False
        
            l+=1
            r-=1
    
        return True


    def isAlphanumeric(self, s: str) -> bool:
        return ('A' <= s <= 'Z') or ('a' <= s <= 'z') or ('0' <= s <= '9')