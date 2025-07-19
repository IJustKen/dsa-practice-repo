# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#this is the more optimized memory efficient one i wrote afterwards, first sol is beneath this one
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #logic is we start from root, wherever the path changes for either of the searches we stop and return it as
        #LCA
        curr = root
        flag = True      #flag to mark that the search for p and q is going together
        while flag:            
            if curr.val > p.val and curr.val > q.val:        #means both p and q in same direction from here
                curr = curr.left
                continue
            if curr.val < p.val and curr.val < q.val:        #p and q in same direction from here
                curr = curr.right
                continue
            if curr.val == p.val and curr.val == q.val:        #both coincide actually doesnt exist but ok
                return curr
            else:                                        #anything else means p and q in different directions which means this must be the LCA rn
                                                        #so we break and return the curr node
                flag = False
        return curr
#kinda bruteforce ish this one fine the path for both then go backwards and see where they first meet
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        curr = root
        while curr:      #find for p
            if not curr:
                break
            if curr.val == p.val:
                path1.append(p)
                break
            elif curr.val>p.val:
                path1.append(curr)
                curr = curr.left
                continue
            elif curr.val<p.val:
                path1.append(curr)
                curr = curr.right
                continue
        
        curr = root
        while curr:            #find for q
            if not curr:
                break
            if curr.val == q.val:
                path2.append(q)
                break
            elif curr.val>q.val:
                path2.append(curr)
                curr = curr.left
                continue
            elif curr.val<q.val:
                path2.append(curr)
                curr = curr.right
                continue
                
        p1,p2 = len(path1)-1,len(path2)-1

        while path1[p1].val != path2[p2].val and p1 >= 0 and p2 >= 0:    #then see their last common ancestor
            if p1>p2:
                p1 -= 1
            elif p1<p2:
                p2 -= 1
            else:
                p1 -= 1
                p2 -= 1
        
        return path1[p1]
        



        
