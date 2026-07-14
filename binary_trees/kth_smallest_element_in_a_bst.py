# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  # the idea was that I will perform inorder traversal which will anyway give me the elements in ascending order
  # from that i just have to return the kth element
  # NOTE: if you do complete traversal and then do res[k-1], it still works but it is unnecessary to scan full tree, only till kth smallest you have to
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []  # empty list
        def inorder(node, k, res):
            if len(res) == k:  # if k elements have been addded to the list, return the list now
                return res
            if node and node.left:  # first check left
                res = inorder(node.left, k, res)

            if node and len(res) != k:  # then check the middle, but also check if the previous step (checking left) already found k elements
                res.append(node.val)

            if node and node.right and len(res) != k:  # check right, but also check if k elements have already been found
                res = inorder(node.right, k, res)

            return res  # return the latest updated res

        return inorder(root, k, res)[-1]  # get the last element from that list
