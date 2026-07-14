# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root and (not root.left and not root.right):
            return root.val  # edge case

        # so we will track the max with the res variable
        def dfs(node, res):  
            if not node:  # reaching a leaf
                return 0, res

            right_gain, res1 = dfs(node.right, res)  # max possible sum gained on the right, V IMP TO PASS res as it is the global max we are keeping track of
            left_gain, res2 = dfs(node.left, res)  # max possible sum gained on the left

            right_gain = max(0, right_gain)  # we only wanna add them, if they are greater than 0
            left_gain = max(0, left_gain)  # else we do not want to add anything at all  

            curr_sum = node.val + left_gain + right_gain  # left gain + curr node + right gain check for every node
            # notice here if left or right gain was negative they contribute nothing and it is like extending from curr node
            # towards only one direction or none at all
            new = max(res, curr_sum, res1, res2)  # maybe max was found while searching in right side or left side hence keep that too
          
            return node.val + max(right_gain, left_gain), new  # finally return the current node's max possible path sum, that is what this function is doing

        return dfs(root, root.val)[1]
    


        
