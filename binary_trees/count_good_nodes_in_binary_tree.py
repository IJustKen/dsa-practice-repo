# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m):
            if not node:  # base case we reached the end of a branch
                return 0
            if node.val >= m:  # case when we increment count 
                return 1 + dfs(node.right, node.val) + dfs(node.left, node.val)
            return dfs(node.right, m) + dfs(node.left, m)  # case when we do not increment count but still go deeper in tree

        return dfs(root, root.val)  # call it
            
        
