class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums = sorted(nums)
        result = []

        while i < len(nums) - 2:
            if i>0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                Sum = nums[i] + nums[j] + nums[k]
                if Sum < 0:
                    j += 1
                elif Sum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                
            i += 1
        return result
