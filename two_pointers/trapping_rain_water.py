# Optimal 2 pointer approach
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)- 1
        left_max, right_max = height[l], height[r]
        water = 0
        # maintain a left and right max variables
        # then move the left and right pointers
        while l<r:
            if height[l] < height[r]:  # in this case the thing that limits how much water can be on top of l'th wall, is the left max wall
                # because for sure on the right we have r'th wall which is taller
                left_max = max(left_max, height[l])  # if the current l'th wall is taller, update it
                water += left_max - height[l]  # if prev wall was taller then we get something, if curr was taller, left max got updated to it, so this gives 0
                l += 1  #move forward
            else:  # height[r] <= height[l]
                right_max = max(right_max, height[r])  # same logic as above limiting factor is the right max now
                water += right_max - height[r]
                r -= 1
        return water




# Approach 2: my initial approach (still O(n) time but also O(n) space)
# make 2 passes in height to store the max observed heights on the left and then on the right
# then one last pass to calculate water on top of each wedge
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]
        right = [0]
        water = 0
        curr = 0
        for i in range(1,n):
            if height[i-1] > curr:
                curr = height[i-1]
            left.append(curr)
        curr = 0
        for i in range(n-2, -1, -1):
            if height[i+1] > curr:
                curr = height[i+1]
            right.append(curr)
        right.reverse()
        for i in range(n):
            water += max(min(left[i], right[i]) - height[i], 0)
        return water
