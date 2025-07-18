# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

  #we doing a recursive way ok. So I shall explain ahead.
  #this function is supposed to return the root of the tree after deletion

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
      
        if not root:          #base case when node is null
            return root
          
        if key > root.val:                              #this means now we perform delete on the right subtree cuz
                                                        #key > current node.val
            root.right = self.deleteNode(root.right,key)
          
        elif key < root.val:              #similarly this means we perform delete on left subtree
            root.left = self.deleteNode(root.left,key)
          
        #we are assigning like this because the next connected node after deletion is done
        #will obv be the root of the right subtree or left subtree after deletion no
      
        else:                    #case when key == node.val, now we do the swap logic
          
            if not root.left:        #nothing on the left means can directly attach right subtree to prev node
                return root.right
              
            elif not root.right:    #similarly directly attach left subtree
                return root.left
            
            curr = root.right      #if both left and right subtree exist then we look for the leftmost elem of right subtree
            while curr.left:
                curr = curr.left
            root.val = curr.val      #then copy its value to root node (current node)
          
            root.right = self.deleteNode(root.right,curr.val)    #then we delete this leftmost node from the right subtree
                                                                #obv then we say "deleted from tree no"
      
        return root      #v imp in the end the function returning root of subtree after deletion only no
        


        
