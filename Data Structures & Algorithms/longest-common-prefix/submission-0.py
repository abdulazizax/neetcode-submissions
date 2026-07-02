class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        s0 = strs[0]

        for i in range(len(s0)):
            for s in strs:
                if i == len(s) or s[i] != s0[i]:
                    return res
            res += s0[i]

        return res