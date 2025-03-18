class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 = digits[::-1]
        list1.append(0)
        for i in range(len(list1)):
            if list1[i] + 1 < 10:
                list1[i] += 1
                break
            else:
                list1[i] = 0
                continue
        
        if list1[-1] == 0:
            list1.pop()
        
        return list1[::-1]
            