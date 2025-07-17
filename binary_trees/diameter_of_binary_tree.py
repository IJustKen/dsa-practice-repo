# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Given the root of a binary tree, return the length of the diameter of the tree.
#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
#This path may or may not pass through the root.
#The length of a path between two nodes is represented by the number of edges between them.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0          #what we maximize (diameter)
        def dfs(node):    #we are basically again finding height but making an update in between
            nonlocal res
            if not node:    #base case null means 0 height  
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
          
            res = max(res, left+right)          #this is the only difference from normal height finding
                                                #diameter is just the sum left max to right side max depth
            return 1 + max(left,right)
        dfs(root)
        return res
        
        


        
