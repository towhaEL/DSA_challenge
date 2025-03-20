class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map = defaultdict(list)

        for item in strs:
            sortedItem = "".join(sorted(item))
            map[sortedItem].append(item)

        for i in map:
            res.append(map[i])
        
        return res