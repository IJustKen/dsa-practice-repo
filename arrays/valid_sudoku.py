from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subboxes = defaultdict(set)  # track subbox numbers
        rows = defaultdict(set)  # track numbers in a row
        cols = defaultdict(set)  # track numbers in a column
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                curr = board[i][j]
                sub_x = i//3  # main trick map each coordinate to a sub box like this
                sub_y = j//3
                if curr == ".":
                    continue
                if curr in rows[i] or curr in cols[j] or curr in subboxes[(sub_x, sub_y)]:
                    return False
                rows[i].add(curr)
                cols[j].add(curr)
                subboxes[(sub_x, sub_y)].add(curr)
        return True
