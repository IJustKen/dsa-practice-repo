from collections import deque
# extension of BFS, logic is basically that for each level of the tree, the right most node will be
# visible, so just maintain an order of the nodes at each level and pick the right most and keep traversing

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        level = []
        res = [root.val]
        while queue:
            node = queue.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
            if not queue:
                if not level:
                    continue
                res.append(level[-1].val)
                for i in level:
                    queue.append(i)
                level = []
        return res






        
