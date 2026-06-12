class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for k, v in enumerate(numbers):
            mp[v] = k 

        print(mp)

        for k, v in enumerate(numbers):
            v1 = target - v
            if v1 in mp:
                return[k+1, mp[v1]+1]

        return []