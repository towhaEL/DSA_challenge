# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next and head.val == val:
            return None

        node = head
        while node and node.next:
            tmp = node
            while tmp.next and tmp.next.val == val:
                tmp = tmp.next

            node.next = tmp.next
            node = node.next

        if head.val == val:
            head = head.next
        return head