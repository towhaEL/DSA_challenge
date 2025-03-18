class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        j=1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                nums[j] = nums[i+1]
                j += 1
        #print(j)
        #nums = nums[:j]   
        return j
  
