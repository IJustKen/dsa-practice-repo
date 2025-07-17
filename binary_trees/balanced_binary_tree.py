# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Check if binary tree balanced, that is, for every node, left and right heights differ by <=1

class Solution:

  #same as height thing again while we update one thing in the middle
  
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True        #assume tree balanced, we will change when contradiction
        def dfs(node):
            nonlocal flag
            if not node:        #base case null height 0
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left-right) > 1:      #this means unbalanced tree so flag False
                flag = False
              
            return 1+max(left,right)

        dfs(root)
        if flag:                          #flag did not go false means balanced
            return True
        else:
            return False
        
        
        
