class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()  # so that we can try solving it similar way as combination sum I 

        def dfs(i, temp, total):
            if total == target:  # base case
                res.append(temp.copy())
                return
            if total > target or i >= len(candidates):  # base case, end the tree
                return
            
            temp.append(candidates[i])  # include the current element 
            dfs(i+1, temp, total + candidates[i])  # include a potential duplicate of the current number eg - [1,1,2,4,5,5], 1 just appended, now this path will 
            # append next 1
            temp.pop()  # once you explore that path, remove the appended element

            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:  # now next path to explore, we do not include the duplicate at all
                i += 1  # thus skip until you get a new element
            dfs(i+1, temp, total)  # explore that path now

        dfs(0, [], 0)
        return res
