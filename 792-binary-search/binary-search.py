class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bSearch(0, len(nums)-1, nums, target)

    def bSearch(self, left, right, nums, target):
        mid = left + (right-left)//2

        if left > right:
            return -1

        if nums[mid] > target:
            return self.bSearch(left, mid-1, nums, target)
        elif nums[mid] < target:
            return self.bSearch(mid+1, right, nums, target)
        else:
            return mid