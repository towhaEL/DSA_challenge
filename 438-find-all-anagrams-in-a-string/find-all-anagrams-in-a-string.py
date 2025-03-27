class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def isAnagram(i, j, str1, str2):
            if sorted(str1[i : j+1]) == str2:
                return True
            else:
                return False

        i = 0
        j = len(p)-1
        ans = []
        str2 = sorted(p)
        while j < len(s):
            if isAnagram(i, j, s, str2):
                ans.append(i)
            i+=1
            j+=1
        return ans