class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for i in s:
            seen[i] = seen.get(i, 0) + 1

        for j in t:
            seen[j] = seen.get(j, 0) - 1

        for k in seen.values():
            if k != 0:
                return False
        
        return True