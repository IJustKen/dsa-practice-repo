# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#insert and return root, any ans is fine as long as it is BST

class Solution:

  #basically we are finding where to insert in this BST
  #so it is like a search only no
  
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
          
            if not node:    #base case prune
                return
              
            if node.val > val:        #search insert pos on the left
                if not node.left:      #if nothing is on left it means insert here
                    node.left = TreeNode(val)
                    return
                else:
                    dfs(node.left)      #else recursively search left subtree
                  
            elif node.val < val:      #same logic as above but for right
                if not node.right:
                    node.right = TreeNode(val)
                    return
                else:
                    dfs(node.right)
        dfs(root)
        if not root:        #edge case when root is None
            return TreeNode(val)
        return root

        
