#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
#candidates where the chosen numbers sum to target. You may return the combinations in any order.

#The same number may be chosen from candidates an unlimited number of times. 
#Two combinations are unique if the frequency of at least one of the chosen numbers is different.

#The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:

  #so again if you look at recursion tree we can either add the curr idx or add the next idx at each step
  #in the end we will get unique subsets only cuz this method only gives unique subsets
  
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def combinator(idx,combo,s):        #idx is the idx in candidates we are deciding to add or not, s is the sum of the combo
            if s == target:
                res.append(combo.copy())
                return
            if s > target or idx >=len(candidates):
                return
            
            combo.append(candidates[idx])        #option 1 choose to add, then next addition can be again idx itself as repetition allowed
            combinator(idx,combo,s+candidates[idx])

            combo.pop()            #option 2 you did not add curr but are checking if the next one can be added
            combinator(idx+1,combo,s)
        
        combinator(0,[],0)
        return res
        
        
