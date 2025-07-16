# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#find max depth of binary tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        def findDepth(node):
            if not node:    #base case
                return 0
            left = node.left
            right = node.right
            return 1 + max(findDepth(left),findDepth(right))    #v logical no need for explanation
        
        return findDepth(root)
        

        
