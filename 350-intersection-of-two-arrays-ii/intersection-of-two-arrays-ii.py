class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=0
        j=0
        nums3 = []
        nums1.sort()
        nums2.sort()
        for k in range(len(nums1)+len(nums2)):
            if i == len(nums1) or j == len(nums2):
                break
            
            if nums1[i] == nums2[j]:
                nums3.append(nums1[i])
                i +=1
                j +=1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                j +=1

        return nums3