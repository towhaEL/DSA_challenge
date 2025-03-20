class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        map = defaultdict(int)
        
        for i in arr:
            map[i] += 1
        
        sorted_map = dict(sorted(map.items(), key= lambda item: item[1], reverse= True))

        sum = 0
        count = 0
        for i in sorted_map:
            if sum < (len(arr)/2):
                sum += sorted_map[i]
                count += 1
        
        return count