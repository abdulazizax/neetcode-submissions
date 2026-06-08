class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, 1
        
        while i < n:
            j = i + 1
            while j < n:
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                j += 1 
            i += 1

        return []