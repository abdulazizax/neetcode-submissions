class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = []

        print(parts)

        for p in parts:
            if stack and p == "..":
                stack.pop()
            elif p != "" and p != ".." and p != '.':
                stack.append(p)
            print("stack ==>", stack)


        return "/" + "/".join(stack)
