class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def valid(nums, max, k):
            c = 1
            total = 0
            for num in nums:
                total += num
                if total > max:
                    c += 1
                    total = num
                    if c > k:
                        return False
            return True
        
        max = 0
        sum = 0
        for num in nums:
            max = num if num>max else max
            sum += num
        l, r = max, sum
        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            if valid(nums, mid, k):
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans

        
        