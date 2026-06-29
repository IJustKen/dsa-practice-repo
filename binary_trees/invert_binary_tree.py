# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # HELPER, to go recursively and solve this
    def dfs(self, node):
        if not node:  # base case stop here
            return
        else:  # otherwise just switch pointers at each level
            temp = node.left
            node.left = node.right
            node.right = temp
        self.dfs(node.left)    # tail recursion, next we do left sub tree
        self.dfs(node.right)    # then right sub tree also, since independent, they can be done one after the other
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.dfs(root)  # since we only playing with pointers in the function call, everything is updated, just need to return root
        return root
