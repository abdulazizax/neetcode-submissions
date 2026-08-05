class NumArray:

    def __init__(self, nums: List[int]):
        self.sumNums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.sumNums[i + 1] = self.sumNums[i] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        return self.sumNums[right + 1] - self.sumNums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)