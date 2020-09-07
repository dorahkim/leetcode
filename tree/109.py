# 109. Convert Sorted List to Binary Search Tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
    
        if head is None:
            return None
        elif head.next is None:
            return TreeNode(head.val)
        
        # find the middle using runner
        walker = head
        runner = head
        while runner is not None:
            if runner.next is None:
                break
            walker = walker.next
            runner = runner.next.next
        
        # root
        root = TreeNode(walker.val)
        
        # root.left
        if head is not walker:
            leftptr = head
            while leftptr.next.val != walker.val:
                leftptr = leftptr.next
            leftptr.next = None
            root.left = self.sortedListToBST(head)

        # root.right
        root.right = self.sortedListToBST(walker.next)
        
        return root
