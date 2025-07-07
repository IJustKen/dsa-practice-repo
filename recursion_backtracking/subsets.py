#Given an integer array nums of unique elements, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
  #example for [1,2,3]
    #imagine a tree basically starting from empty set. Now start from 0th index of nums ok?
  #you can either add it or not add it, thus you get 2 subsets - [] and [1], then further you have choice to add 1st index
  #or not add so you get [],[2]  and [1],[1,2] and so on. This way in the end you will get all subsets
  
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []          #power set
        subset = []        #the subset list that we basically add or not add to 

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())      #append copy to avoid changes with future changes to subset
                return
            subset.append(nums[i])        #this is to decide to add the curr one and proceed
            dfs(i+1)                      #proceeds with added

            subset.pop()                  #this removes the earlier addition essentially making it the
                                          #we ignoring case
            dfs(i+1)                      #and then proceeds with not added also
        
        dfs(0)                        #start from idx 0 so
        return res                    #finally return power set

                

        
