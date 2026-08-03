class Solution:
    def maxDifference(self, s: str) -> int:
        mp = {}

        for i in s:
            mp[i] = mp.get(i, 0) + 1

        maxOdd = 1
        minEven = 1000000

        # print(5%2)
        # print(mp)

        for i in mp:
            if mp[i] % 2 == 0:
                minEven = min(minEven, mp[i])
            else:
                maxOdd = max(maxOdd, mp[i])

        # print("maxOdd ===> ", maxOdd)
        # print("minEven ===> ", minEven)

        return maxOdd - minEven