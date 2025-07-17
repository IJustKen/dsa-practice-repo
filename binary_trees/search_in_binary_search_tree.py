# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#return None if value not found in the tree

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = None      #assume val not there in tree
        def dfs(node):
            nonlocal res
            if not node:    #base case
                return
            if node.val == val:    #found value assign res
                res = node
                return
            elif node.val > val:
                dfs(node.left)
            elif node.val < val:
                dfs(node.right)
        dfs(root)
        return res
        
