class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in indexMap:
                return [i, indexMap[complement]]

            indexMap[nums[i]] = i

       