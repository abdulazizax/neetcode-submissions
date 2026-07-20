class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != "]":
                stack.append(i)
            
            else:
                st = ""
                while stack[-1] != "[":
                    st = stack.pop() + st
                    print("st ==> ", st)

                stack.pop()

                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit

                stack.append(int(digit) * st)

        # print(stack)

        return "".join(stack)

             