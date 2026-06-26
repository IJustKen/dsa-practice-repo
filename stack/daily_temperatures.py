# Monotonic stack problem. Pretty easy: keep adding to stack the temp and its idx, when you encounter a temp which is greater 
# than the top of the stack's value, pop it and the number of days between them will the difference in their indices
# Then again check if that same temp is greater than the new top also, and pop if so and so on. Finally append that temp and carry on.
# MAIN OVERHEAD: Creating tuples and then unpacking each step
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) != 0 and stack[-1][0] < temperatures[i]:
                val, idx = stack.pop()
                answer[idx] = i - idx
            stack.append((temperatures[i], i))
        return answer
