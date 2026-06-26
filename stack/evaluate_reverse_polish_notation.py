# SIMPLE STACK pop twice do operation. Only tricky thing is that you need to save v1 and v2 
# as we need to do v2 {op} v1 and v2 comes after popping twice so CANNOT just do stack.pop() {op} stack.pop()
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        ops = {'+', '*', '-', '/'}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                if token == '+':
                    v1 = stack.pop()
                    v2 = stack.pop()
                    stack.append(v1+v2)
                    continue
                if token == '/':
                    v1 = stack.pop()
                    v2 = stack.pop()
                    stack.append(int(v2/v1))
                    continue
                if token == '-':
                    v1 = stack.pop()
                    v2 = stack.pop()
                    stack.append(v2-v1)
                    continue
                if token == '*':
                    v1 = stack.pop()
                    v2 = stack.pop()
                    stack.append(v1*v2)
                    continue
        return stack[0]
                
        
