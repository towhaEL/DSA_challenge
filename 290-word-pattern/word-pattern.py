class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        Map1 = {}
        Map2 = {}
        if len(pattern) != len(s.split()):
            return False

        for pt, st in zip(pattern, s.split()):
            if pt in Map1 and Map1[pt] != st:
                return False
            if st in Map2 and Map2[st] != pt:
                return False

            Map1[pt] = st
            Map2[st] = pt

        return True