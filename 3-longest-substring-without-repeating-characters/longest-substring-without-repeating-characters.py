class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        i = j = 0

        map = defaultdict(int)

        while j < len(s):
            map[s[j]] += 1

            while map[s[j]] > 1:
                map[s[i]] -= 1
                i += 1

            maxLen = max(maxLen, j-i+1)

            j += 1

        return maxLen