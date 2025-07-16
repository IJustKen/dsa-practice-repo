# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
#inorder is like left - mid - right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def trav(node):    #helper to keep it clean
            nonlocal res
            if not node:      #base case
                return
            trav(node.left)      #recursive
            res.append(node.val)
            trav(node.right)
        trav(root)              #dont forget to call the function lol
        return res
        
