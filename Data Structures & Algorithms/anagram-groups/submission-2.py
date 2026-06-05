class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for i in strs:
            si = "".join(sorted(i)) 
            if si in mp:
                mp[si].append(i)
            else:
                mp[si] = [i]
        
        output = []
        for i in mp:
            output.append(mp[i])

        return output

