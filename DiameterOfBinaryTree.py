# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = [0]
        def dfs(root):
            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            d = rh + lh
            length[0] = max(d, length[0])

            return 1 + max(rh, lh)
        dfs(root)
        return length[0]