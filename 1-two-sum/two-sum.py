class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i in range(len(nums)):
            indexMap[nums[i]] = i 

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in indexMap and i != indexMap[complement]:
                return [i, indexMap[complement]]

       