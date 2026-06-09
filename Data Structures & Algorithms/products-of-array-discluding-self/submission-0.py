class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resp = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            resp[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            resp[i] *= postfix
            postfix *= nums[i]
        
        return resp