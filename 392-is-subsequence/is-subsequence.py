class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        matched = len(s)

        while j < len(t) and i < len(s): 
            if s[i] == t[j]:
                i += 1
                matched -= 1
            j += 1

        if matched == 0:
            return True

        return False
