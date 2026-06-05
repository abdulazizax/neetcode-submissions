class Solution:

    def encode(self, strs: List[str]) -> str:
        resp = ""

        for i in strs:
            resp += str(len(i)) + '#' + i
        
        print(resp)

        return resp

    def decode(self, s: str) -> List[str]:
        resp, i = [], 0
        
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            lengh = int(s[i : j])
            resp.append(s[j + 1 : j + 1 + lengh])
            i = j + 1 + lengh

        return resp