class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        s = "egg"
        s = "add"

        """

        sTot = {}
        tTos = {}

        for s1, t1 in zip(s, t):
            if (s1 in sTot and sTot[s1] != t1) or (t1 in tTos and tTos[t1] != s1):
                return False

            tTos[t1] = s1
            sTot[s1] = t1

        return True