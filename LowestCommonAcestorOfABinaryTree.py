class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(self: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
            if self.val == p or q:
                return self.val
            if not self.right and not self.left:
                return -1
            #Unnecessary check
            if self.val != p or q:
                if self.left and dfs(self.left) != -1:
                    return self.left.val
                if self.right and dfs(self.right) != -1:
                    return self.right.val
                return -1

        curr = root
        while curr:
            if dfs(curr.left, p, q) != -1 and dfs(curr.right, p, q) != -1:
                return curr.val
            elif dfs(curr.left, p, q) != -1:
                curr = curr.left
            else:
                curr = curr.right
