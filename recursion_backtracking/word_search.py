#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cells, where 
#adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# faster solution since we do not use any extra memory for storing "seen"
# idea is to mark visited cell with a random symbol like $ or # or something.
# then restore it while backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word_idx):
            if word_idx >= len(word):    # found the word
                return True

            if i < 0 or i >= len(board):    # base cases to quit
                return False

            if j < 0 or j >= len(board[0]):
                return False

            if board[i][j] != word[word_idx]:
                return False

            temp = board[i][j]    # store the current cell value
            board[i][j] = "$"    # replace with random symbol to mark as visited

            ans = dfs(i+1, j, word_idx+1) or dfs(i-1,j,word_idx+1) or dfs(i, j+1, word_idx+1) or dfs(i, j-1, word_idx+1)
            # search for the word with this cell marked as seen with the $

            board[i][j] = temp    # restore it so that other paths can see it unmarked
            return ans
        
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = res or dfs(i,j,0)
                if res == True:    # early exit condition, saves some time
                    return res
        return res
            




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

         
        
