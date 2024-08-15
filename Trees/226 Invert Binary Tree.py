from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def helper(subtree: Optional[TreeNode]):
        if subtree.left == None and subtree.right == None:
            return 
        else:
            if subtree.right != None:
                helper(subtree.right)
            if subtree.left != None:
                helper(subtree.left)
        left, right = subtree.left, subtree.right
        subtree.left = right
        subtree.right = left
    if root is not None:
        helper(root)
    return root