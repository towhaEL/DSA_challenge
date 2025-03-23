class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = self.bSearch(nums, nums[-1], 0, len(nums)-2)
        print(k)
        if target > nums[-1]:
            ans = self.bSearch1(0, k-1, nums, target)
        elif target < nums[-1]:
            ans = self.bSearch1(k, len(nums)-2, nums, target)
        else:
            return len(nums)-1

        if nums[ans] == target:
            return ans
        else:
            return -1

    def bSearch(self, nums, target, left, right) -> int:
        if left > right:
            return left

        mid = left + (right - left)//2

        if nums[mid] > target:
            return self.bSearch(nums, target, mid+1, right)
        elif nums[mid] < target:
            return self.bSearch(nums, target, left, mid-1)
        else:
            return mid

    def bSearch1(self, left, right, nums, target):
        mid = left + (right-left)//2

        if left > right:
            return -1

        if nums[mid] > target:
            return self.bSearch1(left, mid-1, nums, target)
        elif nums[mid] < target:
            return self.bSearch1(mid+1, right, nums, target)
        else:
            return mid