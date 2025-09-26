class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap = {}
        
        while True:
            if n == 1:
                return True
            hashMap[n] = 1
            p = sum(int(i)**2 for i in str(n))
            n = p

            if n in hashMap:
                return False