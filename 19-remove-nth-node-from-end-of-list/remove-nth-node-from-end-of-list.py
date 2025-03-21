# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        len = 1
        while node.next:
            len += 1
            node = node.next

        node = head
        

        if len == n:
            if n == 1:
                return None
            else:
                head.val = head.next.val
                head.next = head.next.next
        elif n == 1:
            for i in range(len-n-1):
                node = node.next
            node.next = None
        else:
            for i in range(len-n):
                node = node.next
            node.val = node.next.val
            node.next = node.next.next

        return head