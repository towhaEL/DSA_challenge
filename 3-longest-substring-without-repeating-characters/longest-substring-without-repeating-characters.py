class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        start, end = 0, 0
        maxLen = 0

        while end < len(s):
            hashMap[s[end]] = hashMap.get(s[end], 0) + 1
            while hashMap[s[end]] > 1:
                maxLen = max(maxLen, end-start)
                hashMap[s[start]] -= 1
                start += 1

            end += 1

        return max(maxLen, end-start)