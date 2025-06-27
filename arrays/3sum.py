
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
#and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #basically like 2 sum only, this one is O(n^2) though
        #first we sort the nums in ascending order takes nlogn time
        #then here is the logic - of the triplet, pick the first one. Then the remaining becomes the "target" for 2 sum
        #so 2 pointers will work now cuz nums is sorted.
        #KEY LOGIC - AVOIDING duplicate solutions - Do not pick the same first number twice hence the nums[i] == nums[i-1] condition we just skip the iteration
        #cuz if you do your solution repeats
        #similarly after finding a triplet, I increment left such that we reach the next number and avoid duplicating the second num


        nums = sorted(nums)
        n = len(nums)
        solutions = []
        for i in range(n):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            target = -nums[i]       #total target is 0, so remaining target for two sum is this
            left = i+1
            right = n-1
            while left < right:
                
                if target > nums[left] + nums[right]:
                    left += 1
                elif target < nums[left] + nums[right]:
                    right -= 1
                elif target == nums[left]+nums[right]:
                    solutions.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left+1] == nums[left]:      #get the next different number (not same as current left)
                        left += 1   
                    left += 1
                    

        return solutions




            
        