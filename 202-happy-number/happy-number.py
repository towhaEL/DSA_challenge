class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap = {}
        slow = fast = n
        
        while True:
            slow = sum(int(i)**2 for i in str(slow))
            fast = sum(int(i)**2 for i in str(fast))
            fast = sum(int(i)**2 for i in str(fast))
            if slow == fast:
                break

        if slow == 1:
            return True
        else:
            return False

