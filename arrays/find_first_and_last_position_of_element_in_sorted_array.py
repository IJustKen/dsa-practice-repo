#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].

class Solution:

  #Do two binary searches- one to find left extreme the other for the right
  
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        res = []
        while low <= high:    #first binary search to find left extreme
            mid = (high+low)//2
            if nums[mid] == target:    #normally we stop here but now we add an extra condition to check if we are leftmost
                if mid-1>=0:
                    if nums[mid-1] != target:  #conditon 1
                        res.append(mid)
                        break
                    else:
                        high = mid-1    #target found but not leftmost, so we search on left partition
                else:                #condition 2 when no more elem left on the left
                    res.append(mid)                    
                    break
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1

        low = 0
        high = len(nums)-1
        while low <= high:    #same logic but for right everything
            mid = (high+low)//2
            if nums[mid] == target:
                if mid+1<=len(nums)-1:
                    if nums[mid+1] != target:
                        res.append(mid)
                        break
                    else:
                        low = mid+1    #now if target not rightmost we go search right partition no
                else:
                    res.append(mid)
                    break
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
        
        if len(res) == 2:
            return res

        return [-1,-1]
        
