"""
Just binary search, imagine flattening out the matrix, because then it becomes in a sorted order.
Need to translate the flattened index to row, column indices for the actual matrix that is all
"""

class Solution:
    # this helper function will translate the flattened index to row, column
    def _translate(self, num, r, c):
        row = num//c
        col = num%c
        return row, col
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 0 or cols == 0:
            return False

        tot_len = rows*cols
        low = 0 
        high = tot_len - 1

        while low<=high:
            mid = (low+high)//2
            r,c = self._translate(mid, rows, cols)
            #print(f"{r} and {c} which is {matrix[r][c]} and mid {mid}")
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
                continue
            elif matrix[r][c] > target:
                high = mid - 1
                continue
        return False
