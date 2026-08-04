class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsMap = {}

        for i, v in enumerate(nums2):
            numsMap[v] = i

        res = [-1] * len(nums1)

        for i, v in enumerate(nums1):
            index = numsMap[v] + 1

            while index < len(nums2):
                if nums2[index] > v:
                    res[i] = nums2[index]
                    break
                index += 1

        return res