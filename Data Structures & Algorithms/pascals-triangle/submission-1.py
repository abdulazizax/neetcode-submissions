class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]

        res = [[1], [1, 1]]

        for i in range(1, numRows - 1):
            t = [1]

            for j in range(len(res[-1]) - 1):
                print(j, res[-1])
                n = res[-1][j] + res[-1][j + 1]
                t.append(n)

            print()

            t.append(1)
            res.append(t)

        return res

