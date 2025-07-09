#place n queens on nxn board such that they no 2 queens attack each other

class Solution:

  #just like other BT ques we keep track of cells we have seen right?
  #ez to track the row and column attacked but what about diagonal?
  #trick - for a certain positive diagonal, each cell's sum is sum like each cell's coords sum up to the same
  #similarly there is negative diagonal (top left to bottom right types), each cell coords diff is same


  
    def solveNQueens(self, n: int) -> List[List[str]]:

      #i - row, j - col
      
        cols = set()    #j values
        posDiag = set()    #i+j values
        negDiag = set()    #i-j values
        res = []

        board = [['.']*n for i in range(n)]    #create empty board w no queens

        def dfs(row):      #our logic is to place queens row by row
            nonlocal res
            if row == n:    #so if we reach here it means all rows queens got placed
                res.append([''.join(r) for r in board])    #to make each row a string
                return
            if row>n:    #base case
                return
            for col in range(n):      #in each row gotta check each column
              
                if col in cols or row+col in posDiag or row-col in negDiag:
                    continue        #already attacked (like the 'seen' in prev kinda ques)
                
                board[row][col] = 'Q'      #try putting queen
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)

                dfs(row+1)        #see further

                board[row][col] = '.'      #remove queen where you just put (means no putting queen here scenario)
                cols.discard(col)
                posDiag.discard(row+col)
                negDiag.discard(row-col)

        dfs(0)
        return res
        
