# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#check if 2 trees are the same
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node1,node2):                #helper function
            if not node1 and not node2:      #base case when both reach NUll
                return True
            if node1 and node2:              #if both exist then check if they unequal
                if node1.val != node2.val:
                    return False              #obv return False
                return dfs(node1.left,node2.left) and dfs(node1.right,node2.right)    #if they equal we check if the
                                                                                      #left and right subtree also equal
            return False      #case when one of the nodes is NUll other isnt

        return dfs(p,q)
            
        
