class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        path = set()
        def dfs(i,j,idx):
            if idx == len(word):
                return True
            if i<0 or j<0 or i>=m or j>=n or word[idx] != board[i][j] or (i,j) in path:
                return False
            
            path.add((i,j))
            res = dfs(i+1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j-1,idx+1)
            path.remove((i,j))

            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

         
        
