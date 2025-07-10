#same as n queens proble but this time instead of returning the board configs
#just return the total number of unique solutions

class Solution:

  #better refer to n-queens.py
  #ditto same logic as that one

  
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set()
        negDiag = set()
        sols = 0    #keep count of solutions

        def dfs(row):
            nonlocal sols
            if row == n:    #base case what we do is changing that is all
                sols += 1
                return
            for col in range(n):
                if col in cols or row+col in posDiag or row-col in negDiag:
                    continue
                #no need to alter any boards here like before just directly do this
                cols.add(col)        #same logic we are saying we placing queen at row,col
                posDiag.add(row+col)
                negDiag.add(row-col)
              
                dfs(row+1)              

                cols.discard(col)
                posDiag.discard(row+col)
                negDiag.discard(row-col)

        dfs(0)
        return sols


 
        
