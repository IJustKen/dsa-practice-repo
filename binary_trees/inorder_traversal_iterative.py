# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Same inorder but using no recursion

class Solution:

  #logic is like recursion only, recursion stack ki jagah we using an actual stack DS
  
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rec_stack = []                #our own stack to emulate recursion stack
        res = []
        curr = root
        while curr or rec_stack:            #either curr exists or stack non empty
            while curr:                      #curr exists then we go left most node until None
                rec_stack.append(curr)      #keep adding em to stack 
                curr = curr.left
            
            curr = rec_stack.pop()        #once we reach left as Null we pop the top (like the backtrack in recursion)
            res.append(curr.val)
            curr = curr.right            #now we repeat same process on the right subtree
          
        return res

  
