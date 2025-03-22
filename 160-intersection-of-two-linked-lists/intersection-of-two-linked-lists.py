# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        len1 = 0
        len2 = 0
        end1 = ListNode()
        end2 = ListNode()

        while node1:
            len1 += 1
            end1 = node1
            node1 = node1.next
        
        while node2:
            len2 += 1
            end2 = node2
            node2 = node2.next

        if end1 != end2:
            return None

        if len1>len2:
            for i in range(len1-len2):
                headA = headA.next
        elif len1<len2:
            for i in range(len2-len1):
                headB = headB.next

        while headA or headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next


        