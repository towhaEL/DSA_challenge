class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        i = j = 0

        freqMap = defaultdict(int)

        while j < len(s):
            freqMap[s[j]] += 1

            maxFreq = max(freqMap.values())
            currLen = j - i + 1
            while currLen - maxFreq > k:
                freqMap[s[i]] -= 1
                i += 1
                currLen = j - i + 1

            maxLen = max(maxLen, currLen)
            j += 1

        return maxLen
                