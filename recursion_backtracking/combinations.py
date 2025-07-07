#Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#You may return the answer in any order.

class Solution:

  #similar to subset question just base case condition changed
  #the length l is maintained to improve efficiency (time)

  
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
      
        def combinator(i,combo,l):      #i indicates the number from 1 to n, l is the length of combo
            if i > n or l>k:            #when to stop
                if l == k:              #in case only i>n was satisfied this needs to be checked
                    res.append(combo.copy())
                return
                
            combo.append(i)            #option 1 add the curr i to combo and then make more combinations from there
            combinator(i+1,combo,l+1)

            combo.pop()                #options 2 dont add the curr i, instead try the next one and make combos after 
            combinator(i+1,combo,l)      #hence gotta remove the earlier addition
        
        combinator(1,[],0)      #i starts from 1 goes to n, starting combo length is 0
        return res
            
        
