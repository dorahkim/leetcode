# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # record in self.dp
    # key: TreeNode, value: [root.val, max(0, root.left's path sum), max(0, root.right's pathsum)]
    def maxOnePath_dp(self, root: TreeNode):
        self.dp[root] = [root.val]
        if root.left is None and root.right is None:
            self.dp[root].extend([0, 0])
        elif root.left is None:
            self.maxOnePath_dp(root.right)
            self.dp[root].extend([0, max(0, self.dp[root.right][0] + max(self.dp[root.right][1:]))])
        elif root.right is None:
            self.maxOnePath_dp(root.left)
            self.dp[root].extend([max(0, self.dp[root.left][0] + max(self.dp[root.left][1:])), 0])
        else:
            self.maxOnePath_dp(root.left)
            self.maxOnePath_dp(root.right)
            self.dp[root].extend([max(0, self.dp[root.left][0] + max(self.dp[root.left][1:])), \
                                  max(0, self.dp[root.right][0] + max(self.dp[root.right][1:]))])
    
    # return max(root + root.left's path sum + root.right's path sum, self.maxPathSum_dp(root.left), self.maxPathSum_dp(root.right))
    def maxPathSum_dp(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return sum(self.dp[root])
        elif root.left is None:
            return max(sum(self.dp[root]), self.maxPathSum_dp(root.right))
        elif root.right is None:
            return max(sum(self.dp[root]), self.maxPathSum_dp(root.left))
        else:
            return max(sum(self.dp[root]), self.maxPathSum_dp(root.left), self.maxPathSum_dp(root.right))
    
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        self.dp = {}
        self.maxOnePath_dp(root)
        return self.maxPathSum_dp(root)
