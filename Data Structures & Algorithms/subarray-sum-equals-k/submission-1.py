class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

            # print("prefixSums ==> ", prefixSums)
            # print("curSum ==> ", curSum)
            # print("diff ==> ", diff)
            # print("res ==> ", res)
            # print()

        return res
