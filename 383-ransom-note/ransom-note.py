class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}
        count = len(ransomNote)

        for r in ransomNote:
            hashMap[r] = hashMap.get(r, 0) + 1

        for m in magazine:
            if bool(hashMap.get(m, 0)):
                hashMap[m] -= 1
                count -= 1

        return True if count == 0 else False