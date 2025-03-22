# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        k = len(lists)
        x = 0
        

        if all(not l for l in lists):
            return None
        while any(lists):
            min = 1000000
            for i in range(0, k):
                if lists[i]:
                    if lists[i].val <= min:
                        x = i
                        min = lists[i].val

            node.next = lists[x]
            lists[x] = lists[x].next
            node = node.next
        
        return head.next
            