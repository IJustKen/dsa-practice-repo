# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# do not get trapped here and think to do preorder and inorder both and then construct tree from that. An easier approach
# is to do preorder traversal including each leaf's None nodes. That way
# 1,2,N,N,N we can tell 2 is left of 1 and 2 has both child N and N, then 1 has right child N
# 1,2,N,4,N,N,3,N,N we can tell since this is preorder, 2 left of 1, left of 2 is N, right is 4, 4 has both N, then 1 has 3 on right, 3 has both N

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []  # create the list of nodes include N
        def dfs(node):
            nonlocal res
            if not node:
                res.append("N")
                return
            res.append(f"{node.val}")
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)  # return in string format

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 1:  # edge case when root is None
            return None

        stack = []
        data = data.split(",")  # split easier for iterating

        def dfs(idx):
            nonlocal data
            if idx >= len(data):  # base case, out of bounds return None and idx as is (end)
                return None, idx

            if data[idx] != "N":  # valid node encountered, create it
                node = TreeNode(val=int(data[idx]))
                stack.append(0)  # this 0 shows how many of the current node's children have been attached
                node.left, new_idx = dfs(idx+1)  # get left node
                stack[-1] += 1  # increase the count of children for the latest added node, which will be "node"'s itself
                node.right, end_idx = dfs(new_idx)  # get right
                stack[-1] += 1  # increase count again
            
            elif data[idx] == "N":  # def return None, and the next idx
                if stack[-1] == 2:  # case when for the current subtroot, both children have been completely found, pop this subroot
                    stack.pop()
                return None, idx+1   # return None and go to next node

            return node, end_idx  # end idx denotes the idx right after the subtree for this subroot gets over
          
        root, _ = dfs(0)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
