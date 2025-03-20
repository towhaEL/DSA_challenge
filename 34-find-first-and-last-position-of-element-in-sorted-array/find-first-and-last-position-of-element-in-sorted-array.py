class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.bSearch(nums, 0, len(nums)-1, target, [-1, -1])

    def bSearch(self, arr: List[int], left: int, right: int, target: int, res: List[int]) -> List[int]:
        mid = left + (right - left) // 2 
        #res = [-1, -1]

        if right < left:
            return res

  
        if arr[mid] == target:
            if  mid==0:
                res[0] = mid
            elif arr[mid-1] != target:
                res[0] = mid
            else:
                res = self.bSearch(arr, left, mid-1, target, res)
            if mid==len(arr)-1:
                res[1] = mid
            elif arr[mid+1] != target:
                res[1] = mid
            else:
                res =  self.bSearch(arr, mid+1, right, target, res)
        elif arr[mid] > target:
            res = self.bSearch(arr, left, mid-1, target, res)
        else:
            res = self.bSearch(arr, mid+1, right, target, res)

        return res

        