#Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
#For example, the array nums = [0,1,2,4,5,6,7] might become:[4,5,6,7,0,1,2] if it was rotated 4 times.
#[0,1,2,4,5,6,7] if it was rotated 7 times.
#Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
#[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

#Given the sorted rotated array nums of unique elements, return the minimum element of this array.

#You must write an algorithm that runs in O(log n) time.

class Solution:
  
#idea 1 - do same as find peak and then depending on where it is (edge or somewhere in between), we return nums[peak_idx+1]
#or nums[0]

#idea 2 - done here is similar to searching peak, but searching trough this time
  
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[low]<nums[high]:    #this means arr is not rotated so return 0th elem
                return nums[low]
              
            if mid-1>=0 and mid+1<=len(nums)-1:
                if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:    #main condition
                    return nums[mid]
                  
                elif nums[mid]<nums[mid+1]:    #we are in an ascending sequence                   
                    if nums[low]<nums[mid]:    #we are in left sorted half
                        if nums[high]<nums[low]:      #this means smaller sorted half is on right
                            low = mid+1
                    else:                      #search the other half if not the above (got by debugging not intuition)
                        high = mid-1

                elif nums[mid]>nums[mid+1]:    #this can only be if mid is peak elem so next elem must be sequence start
                                                #since it is sorted in ascending order, descending case only happens when peak
                    return nums[mid+1]
                  
            elif mid-1>=0:                    #right edge case
                if nums[mid-1]<nums[mid]:
                    high = low-1
                else:
                    return nums[mid]
            elif mid+1<=len(nums)-1:    #left edge case
                if nums[mid+1]<nums[mid]:
                    low = mid+1
                else:
                    return nums[mid]
            else:          #to account for len = 1 arrays
                return nums[mid]

                        
        return nums[mid]      #just a fail safe lol idk if it is needed






        
