#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


class Solution:

    #logic based on how much water can be on top of a block - depends on the minimum of the maximum of the right and left heights available
    #first idea - use a hashmap to keep track of max left and right heights available at each position.
    #second idea - used here O(1) memory
    #start with assuming a leftmax and rightmax. Now 2 pointers l and r to iterate the list. If max on left side is smaller, we 
    #start iterating from left side incrementing l and checking if we found a new lmax
    #if we do find a new one greater than rmax then next time we gotta start decrementing from r side because now rmax is lower than lmax
    
    #intuition - if i have lmax = 4 and rmax = 2 then this means I have guaranteed 4 on the left, and right I have a smaller one so that is 
    #the bottleneck for now, thus I go from r to see if I get a new line with height more than lmax. Say I get a new height while decrementing
    #from r as 8. Then lmax 6, rmax 8 - so now bottleneck is 6.

    #thing is we dont need to know the true rmax and lmax, just the bottleneck on one side is enough.
    # say heights are [4,5,3,2,1] lmax 4 rmax 1 and we have r at 2. Even though lmax is actually 5 it doesn't matter. Either ways the bottleneck
    #is rmax here cuz it is smaller than a discovered possible lmax


    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        water = 0
        if len(height) <= 2:
            return 0
        while l<r:
            if leftMax < rightMax:
                l+=1 
                leftMax = max(height[l], leftMax)
                water += leftMax - height[l]
            else:
                r-=1
                rightMax = max(height[r], rightMax)
                water += rightMax - height[r]
                
        return water



