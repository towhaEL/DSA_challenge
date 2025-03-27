class Solution:
    def minWindow(self, s: str, t: str) -> str:
        max_len = 10**100
        result = ""
        if len(s) < len(t):
            return result
        map = defaultdict(int)
        for c in t:
            map[c] += 1
        counter = len(map)

        begin = end = 0

        while end < len(s):
            c = s[end]
            if c in map:
                map[c] -= 1
                if map[c] == 0:
                    counter -= 1
            end += 1

            while counter == 0:
                c = s[begin]
                if c in map:
                    map[c] += 1
                    if map[c] > 0:
                        counter += 1
                if end-begin < max_len:
                    result = s[begin:end]
                    max_len = end-begin
                begin += 1

        return result