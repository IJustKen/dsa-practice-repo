#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:

  #similar logic to subsets ques, there at each step we decided whether to include the curr index or not
  #here at each node of the tree notice you have len(nums) options to add initially then for each node len(nums)-1
  #options to add, there is no option of not adding ofc
  #So at each step we either add 1 or 2 or 3 or 4 ...
  #how to do this? use a loop and in it do your recursive function

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []        #the permutation (curr)

        def permutate(perm):
            if len(perm) >= len(nums):      #base case when the length of permutation == len(nums) means we got a permutation
                res.append(perm.copy())
                return
              
            for num in nums:            #each num we decide whether to add or not
                if num not in perm:      #ofc also based on if it is already in perm or not
                    perm.append(num)        #option 1 add the curr num
                    permutate(perm)          #check following perms
                    perm.pop()              #option 2 dont add curr but add the next one by popping the last addition and going to next iteration (next num)
                    
        permutate([])
        return res
        


        
