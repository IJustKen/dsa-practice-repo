#There is an integer array nums sorted in ascending order (with distinct values).
#Prior to being passed to your function, nums is possibly rotated at an unknown 
#pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
#For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:

  #use binary search approach but modified. So we keep two pointers l and r
  #and now our comparison is not just with mid but also with l or r depending on which partition we look at
  #in general we will have 2 ascending order sorted parts right, left and right
  #if target is less than mid, then we either need to search on left of mid or right of mid depending on whether target is
  #smaller than l also
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif nums[mid]>=nums[l]:       #basically mid is part of the left partition         
                if target > nums[mid] or target<nums[l]:   #conditions in left partition when we will have to check right next
                    l= mid+1
                else:
                    r = mid-1    #normal case
            elif nums[mid]<=nums[r]:    #mid is part of right partition
                if target < nums[mid] or target > nums[r]:    #conditions when we have to check left part next
                    r = mid-1
                else:
                    l = mid+1  #normal case
        return -1    #not found
            
        
