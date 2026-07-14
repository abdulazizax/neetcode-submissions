class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = 1

        for n in nums:
            if n >= 0:
                m = min(m, n)

        while m in nums:
            m += 1

        return m 