# makes me hate dsa so much
# the logic is like tracking how much we can extend the current height to the right
# also to the left but that is happening on the way.
# so imagine a height 3 is followed by 1. That 3 cannot be extended any further so we pop it, check its area update the result.
# now we look to push the 1. Now because the previous one (3) was >= 1, it is as if 1 was starting from the previous index itself (basically it can be extended back)
# so we push the 1, but keep its starting index same as starting from wherever extending 3 was possible from.

# thus we keep a stack, tracking the start index of a certain height and the height itself (start_idx, height)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]  # initialize
        res = heights[0]

        for idx, height in enumerate(heights):
            if idx == 0:  # skip first element
                continue
            top_idx = None
            while stack and height < stack[-1][1]:  # pop until the new height encountered is less than or equal to previous ones
                top_idx, top_h = stack.pop()
                area = top_h * (idx - top_idx)  # area = height * (width from where to where this height could be extended, which is curr_idx - its start_idx)
                res = max(res, area)  # update result
            
            if top_idx is not None:
                stack.append((top_idx, height))  # if we had to pop something before (multiple), then we keep the start_idx for the new element same as that
              # because this height could have extended from there
            else:
                stack.append((idx, height))  # if nothing was popped before, keep its actual index itself


        n = len(heights)  
        while stack:  # remaining elements in the stack means these heights could be extended till the end
            top_idx, top_h = stack.pop()
            area = top_h * (n - top_idx)  # so width is n - top_idx
            res = max(res, area)  
        
        return res
            
            
                
