# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        if p.val < root.val and q.val < root.val:
            root = root.left
            if self.containsBoth(root, p.val, q.val):
                
            self.lowestCommonAncestor(root.left, p, q)
        else:
            self.lowestCommonAncestor(root.right, p, q)
    
    def containsBoth(self, root: 'TreeNode', num1: int, num2: int) -> bool:
        return True if self.dfs(root, num1) and self.dfs(root, num2) else False
    
    def dfs(self, root: 'TreeNode', target: int) -> bool:
        if not root:
            return False
        if root.val == target:
            return True
        left = self.dfs(root.left, target)
        right = self.dfs(root.right, target)
        return True if left or right else False

sol = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
print(sol.containsBoth(root, 9, 5))