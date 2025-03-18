class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        j = len(nums)-1
        if j+1==0:
            return 0
        else:
            for i in range(len(nums)):
                if i>=j:
                  break
                if nums[i] == val:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    j -= 1
            
            return len(nums) - nums.count(val)
