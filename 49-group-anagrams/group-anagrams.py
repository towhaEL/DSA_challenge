class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        result = []
        
        for s in strs:
            key = ''.join(sorted(s))
            hashMap[key].append(s)

        for h in hashMap:
            result.append(hashMap[h])

        return result