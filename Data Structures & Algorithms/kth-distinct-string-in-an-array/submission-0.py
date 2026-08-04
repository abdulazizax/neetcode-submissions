class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for i in arr:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for i in arr:
            if count[i] == 1:
                k -= 1
            if not k:
                return i

        return ""

