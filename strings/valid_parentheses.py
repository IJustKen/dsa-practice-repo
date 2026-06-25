# KEY TAKEAWAY: You first tried manually allocating a stack of size len(s)+1 and then 
# indexing it and keeping track of a top pointer. Good for C but not here, here the python list
# append and pop are amortized O(1) operations, it sneakily over allocates each time the array has 
# to increase size so that subsequent appends take O(1) and once in a while when size is 2x or 1.125x-ed
# it gets O(n), but amortized time is O(1) hence faster than manual allocation which will always be allocating
# entire len(s)+1 bytes no matter what
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opener = {'(':')', '{':'}', '[':']'}
        closer = {')', '}', ']'}

        for i in range(len(s)):
            if s[i] in opener:
                stack.append(s[i])
            elif s[i] in closer:
                if len(stack) == 0 or opener[stack[-1]] != s[i]:
                    return False
                else:
                    stack.pop()
                    
        if len(stack) == 0:
            return True
        return False

        
