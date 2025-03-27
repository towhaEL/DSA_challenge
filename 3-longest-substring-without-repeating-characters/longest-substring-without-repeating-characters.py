class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = j = 0
        map = defaultdict(int)
        
        while j < len(s):
            map[s[j]] += 1

            if map[s[j]] > 1:
                while map[s[j]] > 1:
                    map[s[i]] -= 1
                    i += 1
            max_len = max(max_len, j-i+1)
            j += 1

        return max_len
