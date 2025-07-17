# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

  #same as before just the arguments change
  
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1,node2):
            if not node1 and not node2:      #base case
                return True
            if node1 and node2:
                if node1.val != node2.val:    #case when false
                    return False
                return dfs(node1.left,node2.right) and dfs(node1.right, node2.left)
              #for symmetricity we see mirror image, left == right we are checking 
              #hence it is node1.left and node2.right check
            return False
        if not root:          #if no root, true
            return True
        return dfs(root.left,root.right)    #else we check left and right subtree
        
