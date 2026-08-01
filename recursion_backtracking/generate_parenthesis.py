class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_count, close_count, temp):
            nonlocal res
            if close_count > open_count:  # base case more closed brackets in temp than open, def fails
                return
            if close_count == open_count and open_count == n:  # required solution so save it when both counts are equal to n
                res.append("".join(temp.copy()))
                return

            if open_count < n:  # add an open bracket only when count of open brackets is less than total available open brackets
                temp.append("(")
                dfs(open_count+1, close_count, temp)  # check case where we added open bracket here
                temp.pop()
            
            if close_count < open_count:  # check case where we did not add the open bracket in the previous step
              # only possible to add closed bracket when open brackets currently present in temp are more in number, else for sure it will not match
                temp.append(")")
                dfs(open_count, close_count+1, temp)
                temp.pop()
        
        dfs(0,0,[])
        return res
