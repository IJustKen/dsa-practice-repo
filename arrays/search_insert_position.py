#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:    #binary search to find the elem
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
              
        #in case not found now we check the last checked element which did not match target
        if nums[mid] > target:    #if that elem is bigger than target, it means target should be at that index and
                                  #the mid number should be at mid+1 idx
            return mid
        return mid+1      #but if mid elem is smaller then obv target must be at mid+1
