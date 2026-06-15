class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        openB = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in s:
            if i in openB:
                if queue and queue[-1] == openB[i]:
                    queue.pop(-1)
                else:
                    return False

            else:
                    queue.append(i)

        return len(queue) == 0

