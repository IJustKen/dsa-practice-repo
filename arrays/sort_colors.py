#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#What I did - use a hashmap to see which num comes how many times, then afterwards I just gotta modify the list accordingly
#If there are 3 zeroes it means first 3 indices must have 0. Like that. SEE ALTERNATIVE EVEN THO THIS BEAT 100%, it isnt one pass

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_freq = {0:0, 1:0, 2:0}
        for color in nums:
            color_freq[color] += 1
        for i in range(len(nums)):
            if i < color_freq[0]:
                nums[i] = 0
            elif i >= color_freq[0] and i < color_freq[0] + color_freq[1]:
                nums[i] = 1
            else:
                nums[i] = 2



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #logic- low portion should have 0, mid have 1 and high have 2
        #so if mid has 0 we swap with where last low was +1
        #similarly if mid has 2 we swap with where last hi was -1
        #if mid 1 then it is correct, hence increment mid

        lo, mid, hi = 0,0,len(nums)-1
        while mid <= hi:
            if nums[mid] == 0:
                nums[mid],nums[lo] = nums[lo],nums[mid]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[hi] = nums[hi],nums[mid]
                hi -= 1
            

    

        
