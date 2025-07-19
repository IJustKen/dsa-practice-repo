# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#check if given tree is an actual BST (follows its properties)

class Solution:

  #BST property - inorder traversal will always be a list of number in ascending order
  
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def inorder(node):    #get inorder traversal list of the values
            nonlocal res
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
          
        inorder(root)          #dont foget to call inorder lol
      
        if len(res) == 1:      #edge case
            return True
          
        for i in range(1,len(res)):    #otherwise check if ascending order or not, dont do sorted(res) == res, tis expensive
            if res[i] <= res[i-1]:
                return False
        return True


#RECURSIVE SOLUTION

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

      #logic is this - every node has a value range basically starting from root, root can be any damn number
      #so between -inf and +inf. THen the left and right children are restricted to -inf and node.val, node.val and +inf respectively.
      #and so on you go there will always be a minimum and maximum range.
      
        def valid(node,minimum,maximum):      #helper
            if not node:
                return True
            if not (node.val>minimum and node.val<maximum):        #if not in that range means invalid
                return False
            
            return valid(node.left,minimum,node.val) and valid(node.right,node.val,maximum)    #else we see if children are also following BST

        return valid(root, float('-inf'),float('inf'))        #start check from root, since root can be anything range is -inf to +inf

        


        

        


        
