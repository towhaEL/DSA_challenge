class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Map1 = {}
        Map2 = {}

        for sc, tc in zip(s, t):
            if sc in Map1 and Map1[sc] != tc:
                return False
            if tc in Map2 and Map2[tc] != sc:
                return False

            Map1[sc] = tc
            Map2[tc] = sc

        return True
        