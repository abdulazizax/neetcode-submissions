class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = 1
        res = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == 0:
                inc = dec = 1
            elif diff > 0:
                inc, dec = inc + 1, 1
            else:
                inc, dec = 1, dec + 1

            res = max(res, inc, dec)

        return res