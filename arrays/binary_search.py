#basic binary search implemented
#no recursion just pointers better

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while low <= high:    #stopping condition 
            mid = (low+high)//2
            if nums[mid] == target:  
                return mid    #stopping condition
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1

        return -1    #return if not found
        
        
