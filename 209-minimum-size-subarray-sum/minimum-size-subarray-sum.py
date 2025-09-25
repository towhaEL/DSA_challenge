class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        min_len = float('inf')
        Sum = 0

        while end < len(nums):
            Sum += nums[end]

            while Sum >= target:
                min_len = min(min_len, end-start+1)
                Sum -= nums[start]
                start += 1 

            end += 1

        return min_len if not math.isinf(min_len) else 0