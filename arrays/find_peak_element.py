#A peak element is an element that is strictly greater than its neighbors.

#Given a 0-indexed integer array nums, find a peak element, and return its index. 
#If the array contains multiple peaks, return the index to any of the peaks.

#You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always
#considered to be strictly greater than a neighbor that is outside the array.
#You must write an algorithm that runs in O(log n) time.

class Solution:

  #when you say O(logn) instantly think binary search style.
  #see here just have to find a peak, not a specific one so we are searching for the condition
  #nums[mid]>both neighbours mid-1 and mid+1, that is just modified binary search
  
    def findPeakElement(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (high+low)//2
            if mid-1>=0 and mid+1<=len(nums)-1:    #mid is not at the edge of the list 
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:    #check greater than both neighbours
                    return mid
                elif nums[mid]<nums[mid-1]:
                    high = mid-1              #update pointers depending on which side the greater element is present
                elif nums[mid]<nums[mid+1]:
                    low = mid+1
            elif mid-1>=0:      #case when we at the right edge, given that outside the list, everything is -infinity
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    high = mid-1
            elif mid+1<=len(nums)-1:    #we are at the left edge
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    low = mid+1
            else:                      #added case to handle when both neighbours absent (like if len(nums) == 1 case)
                return mid
        
                

        
