class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax

        return arr

        """
           [2,4,5,3,1,2]
                    | | 

        1. [2,4,5,3,2,2]
                  | |
        
        2. [2,4,5,3,2,2]
                | | 
        
        3. [2,4,5,3,2,2]
              | | 

        4. [2,5,5,3,2,2]
            | | 

        4. [5,5,5,3,2,2]
            |  
        """