class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]:
                continue
            b = a+1
            c = b+1
            d = len(nums)-1
            while c<d:
                while c<d:
                    total = nums[a]+nums[b]+nums[c]+nums[d]
                    if total<target:
                        c +=1
                    elif total>target:
                        d -=1
                    else:
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        c +=1
                        while nums[c]==nums[c-1] and c<d:
                            c+=1
                b+=1
                while nums[b]==nums[b-1] and b<len(nums)-2:
                    b+=1
                c = b+1
                d = len(nums)-1

        return res