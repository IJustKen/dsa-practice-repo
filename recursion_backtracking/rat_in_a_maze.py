#Consider a rat placed at position (0, 0) in an n x n square matrix mat[][]. 
#The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 
#'U'(up), 'D'(down), 'L' (left), 'R' (right).

#The matrix contains only two possible values:

#0: A blocked cell through which the rat cannot travel.
#1: A free cell that the rat can pass through.
#Your task is to find all possible paths the rat can take to reach the destination, 
#starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell 
#along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not 
#blocked.
#If no path exists, return an empty list.

#Note: Return the final result vector in lexicographically smallest order.

class Solution:
    # Similar as others
    def ratInMaze(self, maze):
        # code here
        m = len(maze)
        n = len(maze[0])
        seen = set()        #to keep track of cells already explored
        res = []          #final result
        def dfs(i,j,path):
            nonlocal res
            
            if i == m-1 and j == n-1:        #base case we reach end so append the path 
                res.append(''.join(path[:]))    #path is list so convert to string
                return
            
            if i<0 or j<0 or i>=m or j>=n or (i,j) in seen or maze[i][j] == 0:
                return        #base case when out of bounds or already seen or wall came
            
            seen.add((i,j))      #if none of the above then continue exploring
            
            path.append('R')      #check right
            dfs(i,j+1,path)
            path.pop()            #explore next direction
          
            path.append('D')    #check down
            dfs(i+1,j,path)
            path.pop()
          
            path.append('L')    #left
            dfs(i,j-1,path)
            path.pop()
          
            path.append('U')    #up
            dfs(i-1,j,path)
            path.pop()
            
            seen.remove((i,j))    #finally remove i,j from seen so that other paths can use
        
        dfs(0,0,[])
        return sorted(res)      #to return in lexicographic order - dictionary alphabetic order
            
