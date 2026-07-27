class Solution:
    def scoreOfString(self, s: str) -> int:
        l = ord(s[0])
        res = 0

        for i in range(1, len(s)):

            res += abs(ord(s[i]) - l)
            l = ord(s[i])

        return res