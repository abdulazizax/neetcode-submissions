class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        [1,  2,  4,  8] [10, 11, 12, 13] [14, 20, 30, 40]
         0.  1.  2.  3.  4.  5.  6.  7.   8.  9.  10. 11.  
                         0.  1.  2.  3.   0.  1.  2.  3.  
        """

        ROWS, COLS = len(matrix), len(matrix[0])

        print(ROWS, COLS)
        print()

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = (l + r) // 2
            row, col = m // COLS, m % COLS
            print(m, row, col)

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True

        return False

        # UPDATE logs SET end_time = $1 WHERE id IN ($2)