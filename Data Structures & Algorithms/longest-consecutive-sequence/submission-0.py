class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]
        # 2,3,4,5,............,10,..........,20

        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n - 1 not in numSet:
                l = 0
                while n + l in numSet:
                    l += 1
                    longest = max(longest, l)

        return longest