class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = {}

        for i in arr:
            mp[i] = mp.get(i, 0) + 1

        res = -1
        for i in mp:
            if i == mp[i]:
                res = max(res, i)

        return res