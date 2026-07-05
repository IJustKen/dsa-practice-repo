# same as a sorted 2 sum logic, but here heights are not sorted, just have to move the pointer pointing to the lower height
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0
        while l<r:
            h_l = height[l]
            h_r = height[r]
            h = min(h_l, h_r)
            b = r-l
            res = max(res, b*h)
            if h_l < h_r:
                l += 1
            elif h_l > h_r:
                r -= 1
            else:
                l += 1
                r -= 1
        return res
