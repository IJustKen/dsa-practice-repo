# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node:    # base case
                return None
                
            if not ((p.val<node.val and q.val < node.val) or (p.val>node.val and q.val > node.val)):
                # if p is on one side and q is on the other, it means this is the point where they branch out, and this node
                # is the LCA
                return node    # return it hence
                
            if p.val < node.val:    # both on left, search left
                return dfs(node.left, p, q)
            elif p.val > node.val:    # both on right, search right
                return dfs(node.right, p, q)
        
        return dfs(root, p, q)    # call the function from root


        
