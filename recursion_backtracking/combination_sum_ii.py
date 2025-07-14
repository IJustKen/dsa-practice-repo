#same as combination sum but duplicates are present

class Solution:

  #we will do this like SUBSETS II, same kinda logic and ofc Combination Sum I
  
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)      #sort to deal with duplicates properly
        combo = []  

        def dfs(i,s):      #s is the sum of the curr combo, kept for more efficiency in argument rather than doing sum(combo)
            if s > target:    #prune
                return
            if i >= len(candidates):    #check n prune
                if s == target:
                    res.append(combo.copy())
                return
            if s == target:    #append to result
                res.append(combo.copy())
                return
            
            combo.append(candidates[i])    #normal case we include the curr number
            s += candidates[i]
            dfs(i+1,s)
            combo.pop()    #backtrack
            s -= candidates[i]
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1,s)    #case to include the next DIFFERENT number, if you get the same you will get duplicate ans

        dfs(0,0)
        return res 

        
