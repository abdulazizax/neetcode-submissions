class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

        return 0

        """
        mp = {}

        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        for k, v in mp.items():
            if v > 1:
                return k

        return 0
        """