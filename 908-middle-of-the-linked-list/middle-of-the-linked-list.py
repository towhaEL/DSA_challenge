# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        len = 0
        while node:
            len += 1
            node = node.next

        node = head
        for i in range(int(len/2)):
            node = node.next
            #print(len)
        return node
        
        
        
