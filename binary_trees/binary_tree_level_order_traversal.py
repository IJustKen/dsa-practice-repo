from collections import deque
# level order traversal is just BFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # base
            return []
          
        queue = deque()
        queue.append(root)
        res = [[root.val]]
        temp = []  # stores nodes for a level
        while queue:
            node = queue.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not queue:  # as soon as all elements popped it means, the current level is done
                vals = []  # store actual num values of the nodes
                if not temp:  #base case v imp
                    continue
                for i in temp:
                    queue.append(i)  # now put all temp nodes in queue
                    vals.append(i.val)  # and make list of vals of the curr level
                res.append(vals) 
                temp = []
        return res  # finally is a list of lists 

