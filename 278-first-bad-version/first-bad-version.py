# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.bSearch(0, n-1)

    def bSearch(self, left, right) -> int:
        if left == right:
            return left+1

        mid = left + (right-left) // 2

        if isBadVersion(mid+1):
            return self.bSearch(left, mid)
        else:
            return self.bSearch(mid+1, right)