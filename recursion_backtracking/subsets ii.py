#Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:

  #similar to subsets but one key difference while backtracking
  #see the recursion tree and you will see we get duplicate subsets when we decide
  #to add or remove the same number in more than one node
  #also ofc we need to sort the array so that we can progressively move forward

  
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def dfs(i,subs):
            if i >= len(nums):
                res.append(subs[:])
                return
            curr = nums[i]
          
            subs.append(nums[i])      #option one add the num e.g. - 2
            dfs(i+1,subs)

            subs.pop()          #option two dont add but next you wanna start adding from 
                                #a number which wasn't added in the v prev step (e.g. - 2 here)
          
            while i < len(nums)-1 and nums[i+1] == curr:      #hence we do this until we get that
                i += 1
            dfs(i+1,subs)    #then next recursive call we make decision to add the new number or not

      #essentially this is like subsets original ques, but we make sure every number we consider is unique

        dfs(0,[])
        return res

        
