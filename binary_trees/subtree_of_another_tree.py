# So you could have done what dfs is doing with 
# just isSubtree itself using self.isSubtree method, but in python that creates some overhead and is slower
# also when you do an OR statement, using '|' instead of 'or' is slower in recursive trees

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return True
            elif p and q:
                if p.val != q.val:
                    return False
                return same(p.left, q.left) and same(p.right, q.right)
            return False
        
        def dfs(node, sub):
            if not node:
                return False
            if node.val == sub.val:
                if same(node, sub):
                    return True
            return dfs(node.left, sub) or dfs(node.right, sub)
        
        return dfs(root, subRoot)
        
