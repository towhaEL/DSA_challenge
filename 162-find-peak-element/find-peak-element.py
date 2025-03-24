class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.bSearch(nums, 0, len(nums)-1)

    def bSearch(self, nums, left, right) -> int:
        if left == right:
            return left
        mid = left + (right-left)//2

        if nums[mid] > nums[mid+1]:
            return self.bSearch(nums, left, mid)
        else:
            return self.bSearch(nums, mid+1, right)