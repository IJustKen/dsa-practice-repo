class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        max_ar = 0
        while p1<p2:
            ar = min(height[p1],height[p2])*(p2-p1)
            max_ar = max(ar,max_ar)
            if height[p1]<height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_ar
