class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
        