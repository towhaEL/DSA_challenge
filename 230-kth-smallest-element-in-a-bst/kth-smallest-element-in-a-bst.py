# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = 0
        self.ans = 0
        return self.bfs(root, k)

    def bfs(self, node: Optional[TreeNode], k: int) -> int:
        if not node:
            return
        self.bfs(node.left, k)
        self.n += 1
        if self.n == k:
            self.ans = node.val
        self.bfs(node.right, k)

        return self.ans