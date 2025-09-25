class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = k % len(nums)

        nums[:] = nums[::-1]

        nums[:n] = nums[:n][::-1]

        nums[n:] = nums[n:][::-1]


        