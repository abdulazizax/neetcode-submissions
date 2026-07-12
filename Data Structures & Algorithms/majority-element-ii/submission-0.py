class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res, count = [], Counter(nums)

        for k in count:
            if count[k] > len(nums) // 3:
                res.append(k)

        return res