class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        hashSet = [[], [], []]

        for i in nums:
            hashSet[i].append(i)

        i = 0

        for s in hashSet:
            for v in s:
                nums[i] = v
                i += 1

        return None

        