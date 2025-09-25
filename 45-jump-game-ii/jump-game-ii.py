class Solution:
    def jump(self, nums: List[int]) -> int:
        boundary = 0
        max_reach = 0
        min_step = 0

        for i in range(len(nums)):
            if i > boundary:
                boundary = max_reach
                min_step += 1
            max_reach = max(max_reach, nums[i]+i)
            
        return min_step
            
        