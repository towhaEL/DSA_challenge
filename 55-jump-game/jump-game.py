class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p = 0

        for i in range(len(nums)):
            if i > p:
                return False
            p = max(p, i + nums[i])
        
        return True