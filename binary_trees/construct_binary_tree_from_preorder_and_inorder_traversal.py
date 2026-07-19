# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
      
        hashmap = {val: idx for idx, val in enumerate(inorder)}  # this is the main reason the code could optimize and be like O(n)

        # also using indices for tracking the slice of inorder list is better than slicing list and passing as argument each time
        # as each slice operation is O(n)
      
        def get_node(in_left, in_right, subroot_val):
            # creates and returns the node corresponding to subroot_val in the given inorder list slice
            # slice is defined by the in_left and right indices
            nonlocal hashmap
            if subroot_val in hashmap:
                index = hashmap[subroot_val]
                if index <= in_right and in_left <= index:
                    return TreeNode(val=subroot_val), index
            return None, None
          
            # the search below require O(n) time for finding each value, but the above takes O(1). Thus this was ditched.
      
            # for i in range(in_left, in_right+1):
            #     if inorder[i] == subroot_val:
            #         return TreeNode(val=subroot_val), i
            # return None, None
        
        def dfs(preorder_idx, in_left, in_right):
            nonlocal inorder
            nonlocal preorder

            if in_right - in_left < 0:  # edge case, do not put equal to as that is the case when exactly 1 node is present this side
                return None

            if len(preorder) <= preorder_idx:  # all values traversed, edge case
                return None

            node, split_idx = get_node(in_left, in_right, preorder[preorder_idx])  # get the center subroot for current inorder slice
          # which is basically whichever value matches the value of the current preorder list element

            if split_idx is not None:
              # check left of current node in inorder
              # new subroot would possibly be 1 ahead of the current subroot in preorder list
                node.left = dfs(preorder_idx+1, in_left, split_idx-1)
              
              # check right of current node in inorder
              # new subroot would have to be after all the left side nodes are passed from current preorder position
              # that is simply by skipping the number of elements on the left of current subroot which is (split_idx-in_left+1)
                node.right = dfs(preorder_idx+(split_idx-in_left)+1, split_idx+1, in_right)
            return node
        
        return dfs(0, 0, len(inorder)-1)
        
        
            




        
        
