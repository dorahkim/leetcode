# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # return leftmost node of tree
    def leftmost(self, root: TreeNode) -> TreeNode:
        if root.left is None:
            return root
        else:
            return self.leftmost(root.left)
    
    #return rightmost node of tree
    def rightmost(self, root: TreeNode) -> TreeNode:
        if root.right is None:
            return root
        else:
            return self.rightmost(root.right)
        
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        if root.left is not None and root.right is not None:
            if self.leftmost(root.right).val <= root.val or self.rightmost(root.left).val >= root.val:
                return False
        elif root.right is not None:
            if self.leftmost(root.right).val <= root.val:
                return False
        elif root.left is not None:
            if self.rightmost(root.left).val >= root.val:
                return False
        
        # recursion
        return self.isValidBST(root.right) and self.isValidBST(root.left)
