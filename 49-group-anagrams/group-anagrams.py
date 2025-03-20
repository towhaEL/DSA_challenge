class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = sorted(strs, key=sorted)
        ans = []
        tmp = [res[0]]
        for i in range(1, len(res)):
            if sorted(res[i]) == sorted(res[i-1]):
                tmp.append(res[i])
            else:
                ans.append(tmp)
                tmp = [res[i]]
        ans.append(tmp)
        return ans