#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cells, where 
#adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:

    #ok so we keep track of visited cells with path
    #at a curr i,j we first check validity if it aint we say false
    #then we also maintain an idx to keep track of which index of word we are comparing
    #if this reaches len(word) it means all letters have been succesfully compared so this is a solution
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = set()
        
        def dfs(i,j,idx):            #i,j - position, idx is the index in word we are comparing
            
            if idx == len(word):    #base case all letters successfully compared hence idx is now this
                return True
                
            if i<0 or j<0 or i>=m or j>=n or word[idx] != board[i][j] or (i,j) in path:
                return False        #base case when i,j out of bounds or current cell dont match the board[i][j]
                                    #or that (i,j) is in path already (no repeat)

            #neither satisfies so search continues
            
            path.add((i,j))        #add cell to path to explore this certain path
            
            res = dfs(i+1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j-1,idx+1)
            #check all 4 directions
            
            path.remove((i,j))        #remove the cell so it can be used by other paths

            return res
        
        for i in range(m):        #word could start from anywhere so gotta try from everywhere
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

         
        
