# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        head = ListNode()
        node = ListNode()
        tmpNode = ListNode()
        isHead = False

        if not node1 and not node2:
            return None

        while node1 and node2:  
            node = tmpNode         
            tmpNode = ListNode()
            if(node1.val <= node2.val):
                node.val = node1.val
                node.next = tmpNode
                node1 = node1.next
            else:
                node.val = node2.val
                node.next = tmpNode
                node2 = node2.next

            if not isHead:
                head = node
                isHead = True

        if node1:
            while node1:
                node = tmpNode
                tmpNode = ListNode()
                node.val = node1.val
                node.next = tmpNode
                node1 = node1.next
                if not isHead:
                    head = node
                    isHead = True
        elif node2:
            while node2:
                node = tmpNode
                tmpNode = ListNode()
                node.val = node2.val
                node.next = tmpNode
                node2 = node2.next
                if not isHead:
                    head = node
                    isHead = True

        node.next = None
        return head
